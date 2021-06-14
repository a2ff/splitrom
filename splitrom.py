#!/usr/bin/env python3
"""Split a ROM image into individual ROM chips.

Supports interleaved chips and multiple banks.
"""
import sys, functools
def _usage():
    print(F"usage: {sys.argv[0]} <tos.img>"); sys.exit(1)

# knownTos[lang][version][alg][chip] = value
knownTos = {
    'fr': {
        '1.04': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
            'checksum': { 'hi2': 0x0DC8, 'hi1': 0x34A4, 'hi0': 0xE03F,
                          'lo2': 0x8A0C, 'lo1': 0x4AF6, 'lo0': 0x5746 },
            'crc':      { 'hi2': 0x3D94, 'hi1': 0xDB06, 'hi0': 0xE4E9,
                          'lo2': 0x88A2, 'lo1': 0xBC68, 'lo0': 0xEF4C } },
        '1.02': { # from diag cart ST 4.4 in real hw: crc x2-x0 are swapped!
            'checksum': { 'hi2': 0x3158, 'hi1': 0x54C1, 'hi0': 0xF9E0,
                          'lo2': 0x82C4, 'lo1': 0x1BD3, 'lo0': 0x0C15 },
            'crc':      { 'hi2': 0xEB30, 'hi1': 0x201D, 'hi0': 0xB34E,
                          'lo2': 0xB217, 'lo1': 0x35DF, 'lo0': 0xDBAD } },
        '1.00': { # dump of Atari mask ROMs
            'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                          'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
            'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                          'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
    } }
# whichTos[alg][chip][value] = (lang, version)
# whichTosChip[alg][value] = (lang, version, chip)
# example: whichTos['checksum']['hi2'][0x0DC8] = ('french', '1.04')
#          whichTosChip['checksum'][0x0DC8] = ('french', '1.04', 'hi2')
whichTos = {}; whichTosChip = {}
def _initWhichTos():
    for l, v_ in knownTos.items():
        for v, a_ in v_.items():
            for a, c_ in a_.items():
                if a not in whichTos: whichTos[a] = {}
                if a not in whichTosChip: whichTosChip[a] = {}
                for c, s in c_.items():
                    if c not in whichTos[a]: whichTos[a][c] = {}
                    whichTos[a][c][s] = (l, v)
                    whichTosChip[a][s] = (l, v, c)
_initWhichTos()
#import pprint
#pprint.pp(whichTos); pprint.pp(whichTosChip)

def splitRom(rom, chunk = 65536, count = 3, words = ('hi', 'lo')):
    """Split a ROM image into chunk*count chunks of chunk bytes.

    Supports only 8-bit ROM chips.

    rom: the ROM image. Shall be iterable, should be a bytearray.
    chunk: the length of one ROM chip.
    count: the number of banks, for sanity checking as it shall hold that
           len(rom)==chunk*count*len(words)
    words: the name of each ROM chip in a bank.

    return: dictionary of bytearrays of chunk bytes, keyed "{word}{bank}"
            for each word in words and each bank up to count.
    """
    if (l:=len(rom))!=chunk*count:
        print(F"caution, {l} is not {chunk*count//1024}kB")
    return {F"{words[j]}{i}":rom[chunk*i:chunk*(i+1)][j::len(words)]
            for i in range(count) for j in range(len(words))}

def chksum(rom):
    """Compute the Atari Diagnostics Cartridge checksum.

    This is a plain 16-bit modular sum.
    """
    return sum(rom)&0xFFFF

_xmodemCrc = []
def _initCrc():
    for i in range(256):
        t = 0; a = i<<8
        for j in range(8):
            t <<= 1; a <<= 1
            if (t^a)&0x10000: t ^= 0x1021
        _xmodemCrc.append(t&0xFFFF)
_initCrc()

def crc(rom):
    """Compute the Atari Diagnostics Cartridge CRC.

    Atari used the XMODEM CRC.
    Ref: https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem
    """
    return functools.reduce(
            lambda s, i: ((s<<8)&0xFFFF)^_xmodemCrc[(s>>8)^i], rom, 0)

def splitName(file):
    """Split a filename's extension.

    return tuple (basename, extension)
    If there is no extension, use ".img"
    """
    try: base, ext = file.rsplit('.', 1)
    except: base, ext = file, "img"
    return base, "."+ext

def splitFile(file, chunk = 65536, count = 3, words = ('hi', 'lo')):
    """Split a ROM file from disk.
    
    See splitRom() arguments.
    """
    base, ext = splitName(file)
    rom = splitRom(open(file, 'rb').read(), chunk, count, words)
    for n in rom: open(F"{base}-{n}{ext}", 'wb').write(rom[n])

def checkFiles(files):
    """Checksum and identify a list of split ROM files.
    """
    tabs = max([(len(i)+8)//8 for i in files])
    print('\t'*tabs+"chksum\tcrc\tchksum?\t\tcrc?")
    for i in files:
        rom = open(i, 'rb').read(); s = chksum(rom); c = crc(rom)
        print(F"{i}\t{s:04X}\t{c:04X}\t", end='')
        try:
            l, v, r = whichTosChip['checksum'][s]
            print(F"{r} {v}{l}", end='\t')
        except: print(end='\t')
        try:
            l, v, r = whichTosChip['crc'][c]
            print(F"{r} {v}{l}")
        except: print()

def checkFile(*files):
    """Checksum and identify any number of split ROM files.
    """
    checkFiles(files)

def checkSplit(file, chunk = 65536, count = 3, words = ('hi', 'lo')):
    """Checksum and identify a set of split chunks.
    
    See splitRom() arguments.
    """
    base, ext = splitName(file)
    checkFiles([F"{base}-{j}{i}{ext}" for j in words
                                        for i in reversed(range(count))])

def prettySplits(lang, ver, files, count = 3, words = ('hi', 'lo')):
    """Pretty-print the checksums of a list of split ROM files,
    for inclusion in splitrom.py.
    
    Takes a list of files but assumes ordered naming same as splitRom().
    E.g. default args yield hi2, hi1, hi0, lo2, lo1, lo0.
    """
    roms = [open(i, 'rb').read() for i in files]
    sums = [[chksum(i) for i in roms], [crc(i) for i in roms]]
    idx = [F"{j}{i}" for j in words for i in reversed(range(count))]
    idx = dict(zip(idx, range(len(idx))))
    algs = ['checksum', 'crc']
    print(F"    {repr(lang)}: {{\n"
          F"        {repr(ver)}: {{")
    for a in range(len(algs)):
        for i in range(len(words)):
            sa = F"'{algs[a]}':"
            if i==0: print(F"            {sa:11} {{", end='')
            else:    print(F"                         ", end='')
            for j in reversed(range(count)):
                k = idx[F"{words[i]}{j}"]
                print(F" '{words[i]}{j}': 0x{sums[a][k]:04X}", end='')
                if j>0 or i<len(words)-1: print(",", end='')
            if i<len(words)-1: print()
            else:              print(" }", end='')
        if a<len(algs)-1: print(",")
        else:             print(" },")

if __name__=='__main__':
    try:
        f = sys.argv[1]
        splitFile(f)
        checkSplit(f)
    except IndexError: _usage()
    except Exception as e: print(e); _usage()
