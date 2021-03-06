#!/usr/bin/env python3
import sys, splitrom
def _usage():
    print(F"usage: {sys.argv[0]} <version> <ROM dumps in order n..0, hi..lo>"); sys.exit(1)

try:
    splitrom.checkFiles(sys.argv[2:])
    print("\nif ROMs unidentified, add this to splitrom/known.py:")
    splitrom.prettySplits(sys.argv[1], sys.argv[2:], len(sys.argv[2:])//2)
except Exception as e: print(e); _usage()
