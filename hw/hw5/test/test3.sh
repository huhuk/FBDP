#!/bin/bash


NEWPATH='tmp/output-1/part-00000'
OLDPATH='tmp/raw_clusters.txt'

cat $OLDPATH
cat $NEWPATH

T=2
for t in `seq 1 $T`
do
    diff $OLDPATH $NEWPATH
done

#    if [[ ${PIPESTATUS[0]} == "0" ]]; then
#        echo '*'
#break
#    fi

