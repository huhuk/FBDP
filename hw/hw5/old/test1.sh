#!/bin/bash

if [diff output/output-1/part-00000 output/output-2/part-00000 ]; then
    echo 'no diff'
else
    echo 'diff!'
fi

#./pri.py

T="3"
K='*'

if [ ! -z "$1" ]; then
    echo "1st argument is empty!"
    T=$1
fi

echo 'T = '$T

for t in `seq 1 $T`
do
    if [ $t -eq "1" ]; then
        echo 'yes: t = 1'
    else
        echo $K': t-1='$[t-1]
    fi
done

