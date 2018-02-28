#!/usr/bin/python3

import sys

for row, line in enumerate(sys.stdin):
    if len(line.strip().split('\t')) <= 5:
        print(row, len(line.strip().split('\t')), line.strip().split('\t'))


