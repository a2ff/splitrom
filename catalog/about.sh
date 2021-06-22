#!/bin/zsh
for i in *img more/*img ; do echo -n $i ;  strings $i | grep 1985 ; done
