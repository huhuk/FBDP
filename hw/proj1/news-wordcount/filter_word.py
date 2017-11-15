#!/usr/bin/python3

import sys

k = 0
if len(sys.argv) == 3 and sys.argv[1] == '-k':
    k = int(sys.argv[2])

old_key = None
old_values = 0

for line in sys.stdin:
    new_key, new_value = line.strip().split()
    new_value = int(new_value)
    if old_key != new_key:
        if old_values and old_values >= k:
            print('\t'.join([old_key, str(old_values)]))
        old_key = new_key
        old_values = 0
    old_values += new_value


if old_values and old_values > k: 
    print('\t'.join([old_key, str(old_values)]))

