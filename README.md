# TOS (and other ROM) splitter

# `splitrom.py` Python module and executable
`splitrom.py` requires Python 3.9 or higher.
No dependencies beyond the Python standard library.

`splitrom.py` was created to facilitate upgrading Atari ST computers with TOS 1.04.
It can also be used for STe and TT (no need on Falcon, it has a single 16-bit EPROM).
It may or may not be useful for non-Atari computers.

The `splitrom.py` module is also its own executable, which by default will apply ATARI ST TOS 1.x parameters, e.g. 192kB ROM split into 3 chunks of 2 byte lanes.

Parameters other than defaults will be needed for other geometries, e.g. 1 chunk of 4 byte lanes (case of Atari TT) or 1 chunk of 2 byte lanes (case of Atari STe):
- by passing optional parameters to `splitrom.py` (see help in `./import.py`);
- by passing optional parameters to `splitrom.splitFile()` and other functions (see help in `import splitrom; help(splitrom)`) from your own programs.

There is no support for lanes wider than 1 byte (case of 32-bit Amiga, which takes 1 chunk of 2 lanes of 16-bit ROM).

## TOS 1.04 upgrade
ST and STf with 6 mask ROM or UVPROM can be upgraded by inserting 6 newly programmed EPROM chips.
STf with only 2 of the 6 ROM sockets populated can be upgraded to 6 EPROM by moving 3 solder blobs, or straps on the Mega ST.

The 192kB ROM image needs to be split into 3 64kB chunks, which further need to be split into odd and even bytes.
Your EPROMer software may know how to split DWord images and apply an offset,
or you may use `splitrom.py`:
```
 $ ./splitrom.py tos104fr.img
			chksum	crc	chksum?		crc?
tos104fr-hi2.img	0DC8	E4E9	hi2 1.04fr	hi0 1.04fr
tos104fr-hi1.img	34A4	DB06	hi1 1.04fr	hi1 1.04fr
tos104fr-hi0.img	E03F	3D94	hi0 1.04fr	hi2 1.04fr
tos104fr-lo2.img	8A0C	EF4C	lo2 1.04fr	lo0 1.04fr
tos104fr-lo1.img	4AF6	BC68	lo1 1.04fr	lo1 1.04fr
tos104fr-lo0.img	5746	88A2	lo0 1.04fr	lo2 1.04fr
 $ du -h tos104fr*img
 32K	tos104fr-hi0.img
 32K	tos104fr-hi1.img
 32K	tos104fr-hi2.img
 32K	tos104fr-lo0.img
 32K	tos104fr-lo1.img
 32K	tos104fr-lo2.img
192K	tos104fr.img
```

You may now burn 6 `27C256` UVPROM or OTPROM.
Refer to the known motherboards section for which chip goes into what socket.


## Atari Diagnostics Cartridge
The Atari Diagnostics Cartridge version 4.4 ST has a bug: the CRCs are shown in ascending order instead of descending, i.e. **the CRCs of H2 and H0 are swapped, and so are those of L2 and L0.**

Example outputs:
```
ROM checksum test

TOS in ROM: although six ROMs are shown, there may actually be only two.
Version 1.4 French PAL
      checksum	crc
H2	0DC8	3D94
H1	34A4	DB06
H0	E03F	E4E9
L2	8A0C	88A2
L1	4AF6	BC68
L0	5746	EF4C
```

```
ROM checksum test

TOS in ROM: although six ROMs are shown, there may actually be only two.
Version 1.2 French PAL
      checksum	crc
H2	3158	EB30
H1	54C1	201D
H0	F9E0	B34E
L2	82C4	B217
L1	1BD3	35DF
L0	0C15	DBAD
```

`identify.py` will compute the checksum and CRC of ROM chip dumps, identify whether they are of a version known to `splitrom.py` and generate a source code fragment for inclusion into `splitrom.py`, for any number of pairs of 8-bit dumps.

`identify.py` mimics the reverse order in which Atari ST Diagnostics Cartridges list TOS checksums. Other than that, `identify.py` is generic.

Assume you pulled ROM chips from sockets U2..U7 from a motherboard where U2..U7 happens to be the expected order Hi-2, Hi-1, Hi-0, Lo-2, Lo-1, Lo-0, then shell globbing will pass the files in the right order:
```
 $ ./identify.py 1.00fr u?.bin
	chksum	crc	chksum?		crc?
u2.bin	EB83	293D	hi2 1.00fr	hi2 1.00fr
u3.bin	DF2B	31EE	hi1 1.00fr	hi1 1.00fr
u4.bin	F0B9	B603	hi0 1.00fr	hi0 1.00fr
u5.bin	6C4C	9372	lo2 1.00fr	lo2 1.00fr
u6.bin	9AF3	8C69	lo1 1.00fr	lo1 1.00fr
u7.bin	00D4	FD8E	lo0 1.00fr	lo0 1.00fr

if ROMs unidentified, add this to splitrom/known.py:
    '1.00fr': {
        'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                      'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
        'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                      'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
```
Otherwise explicitly list your 6 ROM dumps in the expected order.

The above example initially responded nothing under `chksum? crc?`, then the JSON fragment was added to `known.py`, then the example was rerun and correctly identified that TOS dump.

`identify32.py` will do the same assuming 1 set of 4 ROM dumps with labelling consistent with the TT:
```
identify32.py 3.06uk 128/EEU601.BIN 128/OEU602.BIN 128/EOU603.BIN 128/OOU604.BIN
		chksum	crc	chksum?		crc?
128/EEU601.BIN	C0A1	0000	ee 3.06uk	is valid
128/OEU602.BIN	B810	0000	oe 3.06uk	is valid
128/EOU603.BIN	A89A	0000	eo 3.06uk	is valid
128/OOU604.BIN	72BB	0000	oo 3.06uk	is valid

if ROMs unidentified, add this to splitrom/known.py:
    '3.06uk': {
        'checksum': { 'ee': 0xC0A1,
                      'oe': 0xB810,
                      'eo': 0xA89A,
                      'oo': 0x72BB },
        'crc':      { 'ee': 0x0000,
                      'oe': 0x0000,
                      'eo': 0x0000,
                      'oo': 0x0000 } },
```

**Note:
some chips have the same checksum or CRC across several different TOS images,
notably different languages of a same TOS version, particularly US and UK.**
The identified TOS can be any of the matches, `identify.py` will not try to output multiple matches.

## Other uses
Write your own tools using `import splitrom`.
See the module content with `help(splitrom)` at the Python interactive prompt.
Using `splitrom.py` as an executable command will assume 6-chip TOS of 3 banks of 2 byte-wide chips, but the Python functions can be passed other geometries than those defaults.

The initial version of `splitrom.py` is in `splitrom_simplistic.py`: with no error checking (Python exceptions will still avoid a hard crash) and hardcoding for 3 banks of 16-bit bus split into byte-wide EPROMs, 3 lines of Python code are all you need.

`interleave_simplistic.py` will byte-interleave any number of files.
It was used for joining the 2 ROM images of a diagnostic cartridge.
Because it knows only about interleaving, not banks, it is not adequate for merging a ST TOS dump, but it will work on a TT 4-chip dump because those are a single bank of 4 byte-wide chips, for a 32-bit bus.
The first argument is the output file.
```
 $ ./interleave_simplistic.py out DIASTHIG.EPR DIASTLOW.EPR ; xxd out | head -1      
00000000: fa52 235f 46fc 2700 31fc 000a 8000 4278  .R#_F.'.1.....Bx
```
The diagnostics cartridge magic number is 0xFA52235F.

`mergetos_simplistic.py` will byte-interleave each pair of files and then concatenate the pairs.
This is hardcoded for dumps of byte-wide ROMs forming several banks of a 16-bit bus, such as ST TOS and typical ST cartridges using 8-bit, but will support any even number of files (e.g. 6 for TOS, 2 or 4 for a ST cartridge, ...).
Files shall be ordered in ascending addresses, which implies most-significant byte first.
The first argument is the output file.
```
 $ ./mergetos_simplistic.py out u{4,7,3,6,2,5}.bin ; md5sum out tos100fr.img
25789a649faff0a1176dc7d9b98105c0  out
25789a649faff0a1176dc7d9b98105c0  tos100fr.img
```

`catalog/*.sh` extract various fields from TOS images, good for building a catalog of TOS fingerprints.

Remember those are as close to one-liners as it gets: no error checking, no parametrization.

## TOS revisions
Revisions recognizable by copyright years in the GEM Desktop About box,
version number in ROM image at offset +2 (0xFC0002)
and build date in ROM image at offset +24 (0xFC0018).

The version number in the ROM header is in the form of 2 BCD digits, and there was always confusion how to interpret the 2nd byte:
- 0x0162 is clearly TOS 1.62
- 0x0100 is clearly TOS 1.0
- 0x0102, is that TOS 1.2 or TOS 1.02 ??
- 0x0106, is that TOS 1.6 or TOS 1.06 or TOS 1.60 ??
- 0x0206, is that TOS 2.6 or TOS 2.06 ??

Usage has settled on TOS 1.02, sometimes 1.2, TOS 1.60, rarely 1.06, almost never 1.6, TOS 2.06 and almost never 2.6 nor 2.60. 

### ST, Mega ST, STacy
192kB TOS in 6 mask ROMs or 6 EPROMs (`27C256`).
Later 520 ST, all 1040 ST and all Mega ST and STacy also support TOS in 2 mask ROMs (or 2 EPROM, requiring an adapter board as there are no pin-compatible 28-pin 1Mb EPROMs).

- TOS 0.98 loaded from floppy disk by 16kB ROM
- "Copyright (c) 1985" = TOS 1.0 1985-11-20 (US, UK), 1986-02-06 (German), 1986-04-24 (French)
- "Copyright (c) 1986, 1987" = TOS 1.02 a.k.a 1.2 1987-04-22 (US, UK, French, German), 1987-09-15 (Swedish, Swiss), 1988-05-11 (Spanish)
- "Copyright © 1985,86,87,88" = TOS 1.04 a.k.a. 1.4 early development build
- "Copyright © 1985,86,87,88,89" = TOS 1.04 1989-04-06
- EmuTOS 1.01 2020-12-06 uses version 1.04 for the ST image and 2.06 for the STe image.

According to a 1989 tech note covering TOS upgrade from 2 mask ROMs to 6 mask ROMs on various motherboards, so most likely a TOS 1.04, it would seem Atari never changed the C026329..34 chip p/n for 6-chip TOS.

### STe, Mega STe
256kB TOS in 2 mask ROMs or 2 EPROMs (`27C010`).

- "Copyright © 1985,86,87,88,89" = TOS 1.06 a.k.a. 1.60 1989-07-29 (1.04 + STe support)
- "Copyright © 1985,86,87,88,89" = TOS 1.62 1990-01-01
- "Copyright © 1985,86,87,88,89,90" = TOS 2.05 1990-12-05
- "Copyright © 1985,86,87,88,89,90,91" = TOS 2.06 1991-11-14 US, UK, French, German, Swedish, Swiss (also in ST Book)
- "Copyright © 1985,86,87,88,89,90" = TOS 2.06 1991-11-14 Spanish

### TT
512kB TOS in 4 mask ROMs or 4 EPROMs (`27C010`).

- "Copyright © 1985,86,87,88,89" = TOS 3.00 1990-06-16 (development "TTOS blue")
- "Copyright © 1985,86,87,88,89,90" = TOS 3.01 1990-08-29
- "Copyright © 1985,86,87,88,89,90" = TOS 3.05 1990-12-05 (2.05 + TT support)
- "1985,86,87,88,89,90,91" = TOS 3.06 1991-09-24 US, UK, French, German, Swedish
- "1985,86,87,88,89,90" = TOS 3.06 1991-09-24 Spanish

### ST Book
- "Copyright © 1985,86,87,88,89,90,91,92" = TOS 3.08 1992-03-10 (US), 1993-01-21 (French) (3.06 + ST Book support)

### Falcon
512kB TOS in 1 mask ROMs or 1 EPROMs (`27C4096`).

- "Copyright © 1985-1993" = TOS 4.00 1992-08-11
- "Copyright © 1985-1993" = TOS 4.01 1992-10-02
- "Copyright © 1985-1993" = TOS 4.02 1993-01-26
- "Copyright © 1985-1993" = TOS 4.04 1993-03-08

## Verified Atari ST motherboards
_Verified from owned machines or in person._

### 520ST (not STf) late 1985, ROMs in lower left quadrant, RAMs in lower right
520 ST upgraded to 1MB very much like 520 ST+ so quite possibly factory-made;
handwritten labels could well be from the Atari factory as well.
UVPROM part numbers have not been inspected, to preserve the labels.
``` C070243 rev. C
      ...--------...
.           U8
:
|  Lo-2 U2
| Lo-1 U3   68000
| Lo-0 U4
| Hi-2 U5  68901
| Hi-1 U6                   |
| Hi-0 U7        ...RAMs... |
+---------------------------+
```
French TOS 1.0 in 6 hand-labelled UVPROM:
```
U2 = FRANCE 4/24 H2
U3 = FRANCE 4/24 H1
U4 = FRANCE 4/24 H0
U5 = FRANCE 4/24 L2
U6 = FRANCE 4/24 L1
U7 = FRANCE 4/24 L0
```

**Install 6 `27C256` 200ns or faster** (32kB UVPROM, or `27C256R` OTPROM, or `28C256` EEPROM).

Conversion to 2-ROM TOS is described in Atari tech notes but requires piggy-backing the `74LS11N` on `U8`.

### 520STf ROMs 2 rows under PSU
``` C070523-001 rev. D week 45 1986
+--------------------...
|
++   H2 U2  H1 U3  H0 U4         .
 |   L2 U5  L1 U6  L0 U7         :
++                         68000 |
|                                |
|     ...RAMs...         +-------+
|     ...RAMs...         |
+------------------------+
```
French TOS 1.0 in 6 `RP23256 (c)Atari 1986`:
```
U2 = C026329-002 RP23256 0174 6M3 A0 = Hi-2
U3 = C026330-002 RP23256 0175 6M3 A1 = Hi-1
U4 = C026331-002 RP23256 0176 6M3 A6 = Hi-0
U5 = C026332-002 RP23256 0177 6M3 A5 = Lo-2
U6 = C026333-002 RP23256 0178 6M3 A1 = Lo-1
U7 = C026334-002 RP23256 0179 6M3 A3 = Lo-0
```

**Install 6 `27C256` 200ns or faster.**

### 520STf late 1987, ROMs in lower left quadrant, RAMs under PSU
``` C070789-001 rev. C 1987
.
:    ...RAM...
|              R71 R72 R73
|
| Lo-2 U53     CE       +-----------+
| Lo-1 U62         U68  |  Shifter  |
| Lo-0 U67    U56       | shielding |
| Hi-2 U48              +-----------+
| Hi-1 U59  A16              U65     U66    +---...
| Hi-0 U63  A17   U64 68000       (Blitter) |
+-------------------------------------------+
```
French TOS 1.2 in 2 ROMs date code week 34 of 1987:
```
U63 = HI-0 = C101633 / SHARP JAPAN / (C)1987 ATARI 8734 D
U59 = HI-1 = empty
U48 = HI-2 = empty
U67 = LO-0 = C101634 / SHARP JAPAN / (C)1987 ATARI 8734 D
U62 = LO-1 = empty
U53 = LO-2 = empty
```
_HI/LO-0..2 **is** serigraphied on this motherboard._

If you have a 2-ROM TOS then jumpers `CE`, `A16`, `A17` have a solder blob on `1M` and the `74LS11N` is installed in `U68`.

**If missing, populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

`R71`, `R72`, `R73` are the 3 68ohm resistors that needed to be installed alongside the 16 `41256` DRAM and capacitors for the 512kB->1MB upgrade.
This machine has a slot for the Blitter (socket not soldered).


## Atari ST motherboards pictures from the Internet

**CAUTION: some motherboard may have ROM sockets keyed the wrong way!
The stencils should be oriented correctly.
The safest course of action is to simply follow the orientation of the previously installed ROM chips.**

### 520ST motherboard `C070115`
Same as `C070243` regarding TOS upgrade.
ROM numbering and locations are the same except U2 is not staggered (more shielding was later added to the entire periphery of the PCB).

This is the earliest motherboard. The 260ST and earliest 520ST had only 2 ROM chips `C026036` and `C026037` (apparently 16kB) with a bootloader for loading a TOS disk in RAM. They will accept a 192kB ROM TOS.

**If missing, populate the DIL28 sockets and 220nF capacitors `C1`..`C6`, install 6 `27C256`.**

### 520STf motherboard `C070859`
SMD custom chips instead of PLCC sockets, otherwise same ROM location, numbering and solder blobs as `C070789`.

**If missing, populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

### 520STfm motherboard `C103088 C103253`
These motherboards have *both* `C103088` and `C103253`. They have PLCC custom chips and SMD RAMs.
ROMs are in a single row under the PSU, the unused slots are missing sockets and capacitors.
No high-resolution pictures, but the motherboard has stencils `HI0 ROM FC-H` etc, same as the Mega ST below, and solder blobs are right above the ROMs.

**Populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

### 1040STf motherboard `C103175`
This motherboard has SMD 4-bit DRAM and custom chips, ROM chips are same as `C070789` with all 3 solder blobs near ROM `Hi-0`.

**Populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

### 1040STfm motherboard `C103225`
The motherboard says "ATARI 1040ST", layout is the same as `C707523` but with solder blobs and ROMs numbered same as `C070789`:
```
U48 Hi-2 ROM FE-H
U53 Lo-2 ROM FE-L
U59 Hi-1 ROM FD-H
U62 Lo-1 ROM FD-L
U63 Hi-0 ROM FC-H
U67 Lo-0 ROM FC-L
```
Solder blobs are at the upper right and lower left of the ROM chips.

**Populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

### 520STfm motherboard `C103414`
Essentially identical to `C103175`, the ROMs have both `Hi-0` etc. and `ROM FC-H` etc. stencils.

**Populate the DIL28 sockets and 220nF capacitors, install 6 `27C256` and move the 3 solder blobs to `256K`.**

### Mega ST
All motherboard revisions have the ROMs in the same location right below the 68000 and expansion slot, with "jumpers" in the lower left corner for selecting 6x 256kb or 2x 1Mb ROM chips instead of solder blobs - but actual jumper headers may not be installed, instead 0-ohm resistors may be soldered.

The ROM sockets are numbered the same on all motherboards:
```
U3 HI-2 ROM FE-H
U4 LO-2 ROM FE-L
U6 HI-1 ROM FD-H
U7 LO-1 ROM FD-L
U9 HI-0 ROM FC-H
U10 LO-0 ROM FC-L
```
Rev. B has the "ROM Fx-y" stencils, rev. 4.0 and 5.0 do not.

Some 2-ROM motherboards do not have sockets installed in the 4 unused positions, but the decoupling capacitors appear to be installed (and the installed ROM chips are socketed).

If you have a 2-ROM TOS then jumpers `W2` and `W3` will be bridged 2-3 and jumper `W4` will be unpopulated and a `74LS11` will be installed in `U12`.
*This is the same circuit as later 520STf except there is no way to disconnect the output of the `74LS11`.*

**Populate the missing DIL28 sockets, install 6 `27C256`, move the 0-ohm resistors of jumpers `W2` and `W3` to 1-2, install a strap or 0-ohm resistor in jumper `W4` and remove `U12` or cut pin 12 of `U12`.**

*Some reported success with `U12` still installed -- this is dubious... unless their `74LS11` had died precisely due to a shorted output.
Later Mega ST may have a resistor on the path from pin 12 of `U12` to `W4` and the ROM sockets, in which case it suffices to remove that resistor.*

### STacy
The STacy has TOS 1.04 on a daughterboard with 2 ROM sockets for 1Mb ROMs.
```
U3 = HI C301123-001 French
U4 = LO C301124-001 French
``` 
**Install 2 `27C010` 200ns or faster.**

### 520STe
The 520STe can have a socketed or soldered surface-mounted MC68000 but all motherboard revisions have the ROMs in the same location above the mouse port recess to the right edge.

The ROM sockets are numbered the same on all motherboards and are very clearly labelled `HI` and `LO`:
```
U102 HI
U103 LO
```
**Install 2 `27C010` 200ns or faster** (128kB UVPROM, or `29F010` or `39F010` Flash EPROM).

The 520STe supports 256kb, 512kb and 1Mb ROMs, the later in `27C010` and `27C1000` pinouts thanks to jumpers — only 1Mb EPROM are large enough for the Mega STe TOS.

### Mega STe
All motherboard revisions have the ROMs in the same location in the lower right corner, below the SIMM slots.

The ROM sockets are numbered the same on all motherboards:
```
U206 = hi
U207 = lo
```
**Install 2 `27C010` 150ns or faster.**

The Mega STe has jumpers like the 1040STe.

### Falcon
The Falcon has a 16-bit bus and uses one 16-bit ROM in PLCC44 format.

**Install 1 `27C4096` 150ns or faster in socket `U51`** (512kB UVPROM, or `27PC240`).

### TT
The TT has a 32-bit bus and uses 4 8-bit ROM.
There are several motherboard revisions but only 2 layouts:
early boards have the ROMs to the right,
later boards have the ROMs to the lower left.

The ROM sockets are numbered the same on all motherboards:
```
U601 EE = TT030 TOS UK C301929-002B EE $AB4D
U602 OE = TT030 TOS UK C301930-002B OE $3E68
U603 EO = TT030 TOS UK C301931-002B EO $C5CE
U604 OO = TT030 TOS UK C301932-002B OO $35D7
```
```
U601 EE = TTOS FRA C301933-003C EE $5B92
U602 OE = TTOS FRA C301934-003C OE $807D
U603 EO = TTOS FRA C301935-003C EO $3123
U604 OO = TTOS FRA C301936-003C OO $DCB1
```
`U601` is `D31..24`, `U602` is `D23..16`, `U603` is `D15..8`, `U604` is `D7..0`
=> `EE` is the even byte of the even (16-bit) word or the most significant byte of the (32-bit) long word, `OE` is the odd byte of the even word, `EO` is the even byte of the odd word and `OO` is the odd byte of the odd word or the least significant byte of the long word.

=> `splitrom.py tos404fr.img 524288 1 ee oe eo oo`.

**Install 4 `27C010` 120ns or faster.**


## References
- owned Atari ST machines
- [The LaST Upgrade](https://www.exxoshost.co.uk/atari/last/index.htm) by the most excellent Exxos
- https://temlib.org/AtariForumWiki/index.php/Atari_ST_motherboard_revisions
- https://www.exxoshost.co.uk/forum/viewforum.php?f=41
- https://www.exxoshost.co.uk/forum/viewforum.php?f=53
- http://www.avtandil.narod.ru/tose.html
- http://www.zhell.co.uk/ttpage.html
- http://www.atariancomputing.com/blog/ataritt030revisionguide
- http://msx.fab.free.fr/mpc2/atari/atari16-32/atari16-.htm
- https://www.yaronet.com/topics/187904-le-petit-tt-illustre
- TOS ROM header metadata and country codes: DevPac 3 user manual and https://www.atari-forum.com/viewtopic.php?t=15038

../..
