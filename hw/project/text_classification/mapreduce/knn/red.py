#!/usr/bin/python3

import sys

num = 0
yes = 0

for line in sys.stdin:
    print(line.strip())
    num += 1
    truth, pred = line.strip().split()
    if truth == pred:
        yes+= 1

print(yes / num)

