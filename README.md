# TOS splitter

`splitrom.py` requires Python 3.9 or higher.
No dependencies beyond the Python standard library.

`splitrom.py` was created to facilitate upgrading Atari ST computers with TOS 1.04.
It may or may not be useful for STe, TT, Falcon and non-Atari computers.

## TOS 1.04 upgrade
Very early ST computers with 2 small ROMs can only boot a TOS disk, not be upgraded to ROM TOS.
ST and STf with 6 mask ROM or UVPROM can be upgraded by inserting 6 newly programmed EPROM chips.
STf with only 2 of the 6 ROM sockets populated can be upgraded to 6 EPROM by moving 3 solder blobs.

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

You may now burn 6 27C128 UVPROM or OTPROM.
Refer to the known motherboards section for which chip goes into what socket.


## Atari Diagnostics Cartridge
ST version 4.4 of the diag cart has a bug: the CRCs are shown in ascending order instead of descending, i.e. **the CRCs of H2 and H0 are swapped, and so are those of L2 and L0.**

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

`identify.py` will compute the checksum and CRC of ROM chip dumps, identify whether they are of a version known to `splitrom.py` and generate a source code fragment for inclusion into `splitrom.py`.

Assume you pulled ROM chips from sockets U2..U7 from a motherboard where U2..U7 happens to be the expected order Hi-2, Hi-1, Hi-0, Lo-2, Lo-1, Lo-0, then shell globbing will pass the files in the right order:
```
 $ ./identify.py fr 1.00 u?.bin
	chksum	crc	chksum?		crc?
u2	EB83	293D	hi2 1.00fr	hi2 1.00fr
u3	DF2B	31EE	hi1 1.00fr	hi1 1.00fr
u4	F0B9	B603	hi0 1.00fr	hi0 1.00fr
u5	6C4C	9372	lo2 1.00fr	lo2 1.00fr
u6	9AF3	8C69	lo1 1.00fr	lo1 1.00fr
u7	00D4	FD8E	lo0 1.00fr	lo0 1.00fr

if ROMs unidentified, add this to splitrom.py:
    'fr': {
        '1.00': {
            'checksum': { 'hi2': 0xEB83, 'hi1': 0xDF2B, 'hi0': 0xF0B9,
                          'lo2': 0x6C4C, 'lo1': 0x9AF3, 'lo0': 0x00D4 },
            'crc':      { 'hi2': 0x293D, 'hi1': 0x31EE, 'hi0': 0xB603,
                          'lo2': 0x9372, 'lo1': 0x8C69, 'lo0': 0xFD8E } },
```
Otherwise explicitly list your 6 ROM dumps in the expected order.


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

`mergerom_simplistic.py` will byte-interleave each pair of files and then concatenate the pairs.
This is hardcoded for dumps of byte-wide ROMs forming several banks of a 16-bit bus, such as ST TOS.
Files shall be ordered in ascending addresses, which implies most-significant byte first.
The first argument is the output file.
```
 $ ./mergerom_simplistic.py out u{4,7,3,6,2,5}.bin ; md5sum out tos100fr.img
25789a649faff0a1176dc7d9b98105c0  out
25789a649faff0a1176dc7d9b98105c0  tos100fr.img
```

Remember those are as close to one-liners as it gets: no error checking, no parametrization.

## TOS revisions
- 1985 = TOS 1.0
- 1987 = TOS 1.02
- 1989 = TOS 1.04

According to a 1989 tech note covering TOS upgrade from 2 mask ROMs to 6 mask ROMs on various motherboards, so most likely a TOS 1.04, it would seem Atari never changed the C026329..34 chip p/n for 6-chip TOS.

### Early 520STf with French TOS 1.0 in 6 `RP23256 (c)Atari 1986`
```
U2 = Hi-2 = C026329-002 RP23256 0174 6M3 A0
U3 = Hi-1 = C026330-002 RP23256 0175 6M3 A1
U4 = Hi-0 = C026331-002 RP23256 0176 6M3 A6
U5 = Lo-2 = C026332-002 RP23256 0177 6M3 A5
U6 = Lo-1 = C026333-002 RP23256 0178 6M3 A1
U7 = Lo-0 = C026334-002 RP23256 0179 6M3 A3
```
_Hi/Lo-0..2 is not serigraphied on this motherboard._

### Late 1987 520STf with French TOS 1.2 in 2 ROMs date code week 34 of 1987
```
U63 = HI-0 = C101633 / SHARP JAPAN / (C)1987 ATARI 8734 D
U59 = HI-1 = empty
U48 = HI-2 = empty
U67 = LO-0 = C101634 / SHARP JAPAN / (C)1987 ATARI 8734 D
U62 = LO-1 = empty
U53 = LO-2 = empty
```

### 1985 ST with French TOS 1.0 in 6 UVPROM
```
TODO
```

## Atari ST motherboards

### 520ST (not STf) late 1985, ROMs in lower left quadrant, RAMs in lower right
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
520ST, ST+, 260ST, should have 6 EPROM.
Early machines have only 2 EPROM with a boot ROM for loading TOS from disk.

**Install the 6 EPROM.**

Conversion to 2-ROM TOS is described in Atari tech notes but requires piggy-backing the `74LS11N` on `U8`.

### 520STf ROMs 2 rows under PSU
``` C0707523-001 rev. D week 45 1986
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

**Install the 6 EPROM.**


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
If you have a 2-ROM TOS then jumpers `CE`, `A16`, `A17` have a solder blob on `1M` and the `74LS11N` is installed in `U68`.

**Install the 6 EPROM and move the 3 solder blobs to `256K` (as in `27C256`, 256kb EPROM).**

`R71`, `R72`, `R73` are the 3 68ohm resistors that needed to be installed alongside the 16 `41256` DRAM and capacitors for the 512kB->1MB upgrade.
This machine has a slot for the Blitter (socket not soldered).

## References
- owned Atari ST machines
- https://temlib.org/AtariForumWiki/index.php/Atari_ST_motherboard_revisions
- https://www.exxoshost.co.uk/forum/viewforum.php?f=41
- https://www.exxoshost.co.uk/forum/viewforum.php?f=53

../..
