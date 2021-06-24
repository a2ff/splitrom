#!/bin/zsh
for i in etos?????.img ; do echo ; echo $i ; splitrom.py $i ; j=${i%.img} ; k="EmuTOS 1.01${j#etos???} ST"; identify.py $k ${i%.img}-{hi,lo}{2,1,0}*
