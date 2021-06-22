#!/bin/zsh
for i in *img more/*img ; do echo -n $i ; dd if=$i bs=1 count=4 skip=24 2>/dev/null | xxd -g4 | cut -d: -f2 | sed 's/^ \(..\)\(..\)\(....\).*/ \3-\1-\2/' ;done 

