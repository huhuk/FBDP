#!/usr/bin/python3

import sys
from math import log

reducer_num = 4

for line in sys.stdin:
    k, v = line.strip().split()
    p = reducer_num - 1 - int(log(int(v)) / log(10))
    print('\t'.join([str(p), v, k]))

