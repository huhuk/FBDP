#!/usr/bin/python3

import sys

old_key = None
old_values = 0

for line in sys.stdin:
    new_key, _ = line.strip().split()
    if old_key != new_key:
        if old_values: 
            print('\t'.join([old_key, str(old_values)]))
        old_key = new_key
        old_values = 0
    old_values += 1

if old_values: 
    print('\t'.join([old_key, str(old_values)]))

