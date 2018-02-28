#!/usr/bin/python3

import sys

old_key = None
t_count = 0
t_x = t_y = 0

for line in sys.stdin:
    new_key, val = line.strip().split('\t', 1)
    count, x, y = ( float(i) for i in val.split() )
    count = int(count)
    if old_key != new_key:
        if t_count != 0:
            print(old_key, t_x/t_count, t_y/t_count, t_count, sep='\t')
        old_key = new_key
        t_count = t_x = t_y = 0
    t_count += count
    t_x += x
    t_y += y
        
if t_count != 0:
    print(old_key, t_x/t_count, t_y/t_count, t_count, sep='\t')


