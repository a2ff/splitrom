#!/usr/bin/env python3
import sys, splitrom
def _usage():
    print(F"usage: {sys.argv[0]} <country> <version> <ROM dumps in order n..0, hi..lo>"); sys.exit(1)

try:
    splitrom.checkFiles(sys.argv[3:])
    print("\nif ROMs unidentified, add this to splitrom.py:")
    splitrom.prettySplits(sys.argv[1], sys.argv[2], sys.argv[3:])
except Exception as e: print(e); _usage()
