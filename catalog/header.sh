#!/bin/zsh
for i in *img more/*img ; do echo $i ; xxd $i |head -2 ;done
