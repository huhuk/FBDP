#!/usr/bin/python3

import numpy as np

N = 20
D = 2
a = 0
b = 10
l = list()
l.append(np.random.randint(a, b, (N, D)))
a = 12
b = 20
l.append(np.random.randint(a, b, (N, D)))
p = np.vstack(l)

for i in p:
    print('\t'.join(i.astype('str')))



