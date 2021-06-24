#!/bin/zsh
for i in tos?????.img ; do echo ; echo $i ; splitrom.py $i ; j=${i%.img} ; k=${j#tos}; identify.py $k ${i%.img}-{hi,lo}{2,1,0}* ; done
