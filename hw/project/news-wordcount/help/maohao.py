#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    print(' '.join(line.split(':')[1:-1])[2:-4].strip())

