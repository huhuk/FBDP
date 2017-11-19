#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    print(' '.join(line.split()[4:-1]).strip())

