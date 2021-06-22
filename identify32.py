#!/usr/bin/env python3
import sys, splitrom
def _usage():
    print(F"usage: {sys.argv[0]} <version> <ROM dumps in order EE OE EO OO>"); sys.exit(1)

try:
    splitrom.checkFiles(sys.argv[2:])
    print("\nif ROMs unidentified, add this to splitrom/known.py:")
    splitrom.prettySplits(sys.argv[1], sys.argv[2:], 1, ('ee', 'oe', 'eo', 'oo'))
except Exception as e: print(e); _usage()
