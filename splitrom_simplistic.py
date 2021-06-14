#!/usr/bin/env python3
import sys
name = sys.argv[1]; base, ext = name.rsplit('.', 1)
rom = open(name, 'rb').read(); l = len(rom)
[open(base+'-'+('lo' if j%2 else 'hi')+f'{i}.'+ext,'wb').write(rom[l//3*i:l//3*(i+1)][j::2]) for i in range(3) for j in range(2)]
