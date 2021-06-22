#!/usr/bin/env python3
"""Split a ROM image into individual ROM chips.

Supports interleaved chips and multiple banks.
"""
import sys, functools
def _usage():
    print(F"usage: {sys.argv[0]} <rom.img> [<chunk size> [<# of banks> [<names of each byte lane>...]]]")
    sys.exit(1)

from known import knownRom
# knownRom[version][alg][chip] = value
# whichRom[alg][chip][value] = version
# whichRomChip[alg][value] = (version, chip)
# example: whichRom['checksum']['hi2'][0x0DC8] = '1.04fr'
#          whichRomChip['checksum'][0x0DC8] = ('1.04fr', 'hi2')
whichRom = {}; whichRomChip = {}
def _initWhichRom():
    for v, a_ in knownRom.items():
        for a, c_ in a_.items():
            if a not in whichRom: whichRom[a] = {}
            if a not in whichRomChip: whichRomChip[a] = {}
            for c, s in c_.items():
                if c not in whichRom[a]: whichRom[a][c] = {}
                whichRom[a][c][s] = v
                whichRomChip[a][s] = (v, c)
_initWhichRom()
#import pprint
#pprint.pp(whichRom); pprint.pp(whichRomChip)

def splitRom(rom, chunk = 65536, count = 3, lanes = ('hi', 'lo')):
    """Split a ROM image into chunk*count chunks of chunk bytes.

    Supports only 8-bit ROM chips.

    rom: the ROM image. Shall be iterable, should be a bytearray.
    chunk: the length of one ROM chip.
    count: the number of banks, for sanity checking as it shall hold that
           len(rom)==chunk*count*len(lanes)
    lanes: the name of each ROM chip in a bank.

    return: dictionary of bytearrays of chunk bytes, keyed "{lane}{bank}"
            for each lane in lanes and each bank up to count.
    """
    if (l:=len(rom))!=chunk*count:
        print(F"caution, {l} is not {chunk*count//1024}kB")
    return {F"{lanes[j]}{i}":rom[chunk*i:chunk*(i+1)][j::len(lanes)]
            for i in range(count) for j in range(len(lanes))}

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

def splitFile(file, chunk = 65536, count = 3, lanes = ('hi', 'lo')):
    """Split a ROM file from disk.
    
    See splitRom() arguments.
    """
    base, ext = splitName(file)
    rom = splitRom(open(file, 'rb').read(), chunk, count, lanes)
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
            v, r = whichRomChip['checksum'][s]
            print(F"{r} {v}", end='\t')
        except: print(end='\t')
        try:
            v, r = whichRomChip['crc'][c]
            print(F"{r if c!=0 else 'is'} {v if c!=0 else 'valid'}")
        except: print()

def checkFile(*files):
    """Checksum and identify any number of split ROM files.
    """
    checkFiles(files)

def checkSplit(file, chunk = 65536, count = 3, lanes = ('hi', 'lo')):
    """Checksum and identify a set of split chunks.
    
    See splitRom() arguments.
    """
    base, ext = splitName(file)
    checkFiles([F"{base}-{j}{i}{ext}" for j in lanes
                                        for i in reversed(range(count))])

def prettySplits(ver, files, count = 3, lanes = ('hi', 'lo')):
    """Pretty-print the checksums of a list of split ROM files,
    for inclusion in splitrom.py.
    
    Takes a list of files but assumes ordered naming same as splitRom().
    E.g. default args yield hi2, hi1, hi0, lo2, lo1, lo0.
    """
    roms = [open(i, 'rb').read() for i in files]
    sums = [[chksum(i) for i in roms], [crc(i) for i in roms]]
    idx = [F"{j}{i}" for j in lanes for i in reversed(range(count))]
    idx = dict(zip(idx, range(len(idx))))
    algs = ['checksum', 'crc']
    print(F"    {repr(ver)}: {{")
    for a in range(len(algs)):
        for i in range(len(lanes)):
            sa = F"'{algs[a]}':"
            if i==0: print(F"        {sa:11} {{", end='')
            else:    print(F"                     ", end='')
            for j in reversed(range(count)):
                k = idx[F"{lanes[i]}{j}"]
                print(F" '{lanes[i]}{j if count>1 else ''}':"
                      F" 0x{sums[a][k]:04X}", end='')
                if j>0 or i<len(lanes)-1: print(",", end='')
            if i<len(lanes)-1: print()
            else:              print(" }", end='')
        if a<len(algs)-1: print(",")
        else:             print(" },")

def tosVersion(file):
    """Display TOS version and date.
    """
    rom = open(file, 'rb').read(32)
    try:
        lang = ("US", "German", "French", "UK", "Spanish", "Italian",
                "Swedish", "Swiss French", "Swiss German", "Turkish",
                "Finnish", "Norwegian", "Danish", "Saudi", "Dutch")[rom[29]>>1]
    except:
        lang = "multi-lingual"
    print("If this is a TOS rom, then it is"
          F" v{rom[2]:x}.{rom[3]:02x}"
          F" {rom[26]:02x}{rom[27]:02x}-{rom[24]:02x}-{rom[25]:02x}"
          F" {'PAL' if rom[29]&0x01 else 'NTSC'} {lang}")

if __name__=='__main__':
    try:
        args = sys.argv[1:]
        if len(args)>3: args[3] = args[3:]; del args[4:]
        if len(args)>2: args[2] = int(args[2])
        if len(args)>1: args[1] = int(args[1])
        tosVersion(args[0])
        splitFile(*args)
        checkSplit(*args)
    except IndexError: _usage()
    except Exception as e: print(e); _usage()
