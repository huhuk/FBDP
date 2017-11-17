#!/usr/bin/python3

import sys

old_key = None
old_count = 0
old_x = old_y = 0

for line in sys.stdin:
    new_key, val = line.strip().split('\t', 1)
    x, y = ( float(i) for i in val.split() )
    if old_key != new_key:
        if old_count != 0:
            print(old_key, old_count, old_x, old_y, sep='\t')
        old_key = new_key
        old_count = old_x = old_y = 0
    old_count += 1
    old_x += x
    old_y += y

if old_count != 0:
    print(old_key, old_count, old_x, old_y, sep='\t')

