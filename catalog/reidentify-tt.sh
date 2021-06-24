#!/bin/zsh
for i in tos30???.img ; do echo ; echo $i ; splitrom.py $i 524288 1 ee oe eo oo ; j=${i%.img} ; k=${j#tos}; identify32.py $k ${i%.img}-{ee,oe,eo,oo}* ; done
