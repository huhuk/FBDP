#!/usr/bin/python3

import sys
from math import log

reducer_num = 4
base = 200000

for line in sys.stdin:
    v, k = line.strip().split()
    new_k = base - int(k)
    print('\t'.join([str(new_k), v]))

