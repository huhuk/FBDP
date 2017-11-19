#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt

filename = 'tmp/output-3/part-00000'
cls = list()
with open(filename, 'r') as f:
    for line in f:
        l = line.strip().split()[:-1]
        l[0] = int(l[0].split('-')[-1])
        l[1] = float(l[1])
        l[2] = float(l[2])
        cls.append(l)

def dist(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)

def find_cl(x, y):
    res = None
    min_d = -1
    for i in cls:
        now_d = dist(i[1], i[2], x, y)
        if res == None or now_d < min_d:
            min_d = now_d
            res = i[0]
    return res

samples_f = 'samples.txt'
ans = list()
with open(samples_f, 'r') as f:
    for line in f:
        x, y = ( float(i) for i in line.strip().split() )
        ans.append( (x, y, find_cl(x, y)) )
ans = np.array(ans)

plt.scatter(ans[:, 0], ans[:, 1], c=ans[:, 2])
plt.savefig('cluster.png')

