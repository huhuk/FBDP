#!/usr/bin/python3

import sys

seperator = '\t'
old_key = None

for line in sys.stdin:
    new_key, value = line.strip().split(seperator, 1)
    value = value.replace(seperator, '#')
    if old_key != new_key:
        if old_key != None:
            print()
        print(new_key, end = '')
        print(':' + value, end = '')
        old_key = new_key
    else:
        print(',' + value, end = '')

