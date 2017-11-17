#!/usr/bin/python3

import sys
import random

filename = './tmp/samples.txt'

k = 3
if len(sys.argv) > 1:
    k = int(sys.argv[1])
if len(sys.argv) > 2:
    filename = sys.argv[2]

with open(filename, 'r') as f:
    l = f.readlines()

for i, j in enumerate(random.sample(l, k)):
    print('cl-' + str(i), j.strip(), 0, sep='\t')

