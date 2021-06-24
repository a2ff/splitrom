#!/bin/zsh
for i in etos?????.img ; do echo ; echo $i ; splitrom.py $i 262144 1 ; j=${i%.img} ; k="EmuTOS 1.01${j#etos???} STe"; identify.py $k ${i%.img}-{hi,lo}* ; done
