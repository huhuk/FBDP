#!/usr/bin/python3

import sys

base = 200000

for line in sys.stdin:
    key, val = line.strip().split()
    new_key = base - int(key)
    print('\t'.join([ str(new_key), val ]))

