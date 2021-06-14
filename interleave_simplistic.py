#!/usr/bin/env python3
import sys
chips = [open(i, 'rb').read() for i in sys.argv[2:]]
rom = bytearray(sum(map(len, chips)))
for i in range(len(sys.argv[2:])): rom[i::len(sys.argv[2:])] = chips[i]
open(sys.argv[1], 'wb').write(rom)
