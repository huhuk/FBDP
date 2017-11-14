#!/usr/bin/python3

import sys

old_key = None
old_values = list()

for line in sys.stdin:
    new_key, docid, url = line.strip().split()
    if old_key != new_key:
        if len(old_values) != 0:
            print(old_key + ':' + ','.join(old_values))
        del old_values
        old_key = new_key
        old_values = list()
    old_values.append('#'.join([docid, url]))

if len(old_values) != 0:
    print(old_key + ':' + ','.join(old_values))

