#!/usr/bin/python3

import sys
import os

def get_content(filename):
    with open(filename, 'r') as f:
        s = f.read().strip()
    return s

f1 = sys.argv[1]
f2 = sys.argv[2]

s1 = get_content(f1)
s2 = get_content(f2)

if s1 == s2:
    os.system('touch tmp/123')

