#!/bin/zsh
for i in tos?????.img ; do echo ; echo $i ; splitrom.py $i 262144 1 ; j=${i%.img} ; k=${j#tos}; identify.py $k ${i%.img}-{hi,lo}* ; done
