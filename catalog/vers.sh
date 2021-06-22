#!/bin/zsh
for i in *img more/*img ; do echo -n $i ; dd if=$i bs=1 count=2 skip=2 2>/dev/null | xxd | cut -d: -f2 ;done 
