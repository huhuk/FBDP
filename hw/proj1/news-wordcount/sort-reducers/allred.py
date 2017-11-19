#!/usr/bin/python3

import sys

o = None
ol = list()

for line in sys.stdin:
    p, k, v = line.strip().split()
    if o != k:
        ol.sort()
        for i in ol:
            print('%s\t%s'%(o, i))
        o = k
        del ol
        ol = list()
    ol.append(v)

ol.sort()
for i in ol:
    print('%s\t%s'%(o, i))

