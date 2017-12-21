#!/usr/bin/python3

import sys
import pickle
import numpy as np
import scipy as sp
from sklearn.feature_extraction.text import TfidfVectorizer

k = 3

def load(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj

# count_vec = load('./tfidf.model')
x_train = load('./x_train.model')
y_train = load('./y_train.model')
x_test = load('./x_test.model')
n = x_train.shape[0]
one = sp.sparse.csr_matrix(np.ones(n).reshape((n,1)))

def get_dist(x):
    dists = sp.sparse.linalg.norm((x_train - one * x), axis=1)
    return sorted(zip(dists, y_train))[:k]


def get_cl(x):
    aDict = dict()
    cls = get_dist(x)
    for j, i in cls:
        if i not in aDict:
            aDict[i] = 1
        else:
            aDict[i] += 1
    if len(aDict) == 3:
        ret = cls[0][1]
    else:
        for i, j in aDict.items():
            if int(j) > 1:
                ret = i
    return ret

for i, line in enumerate(sys.stdin):
    y= line.strip()
    x = x_test[i]
    print(y, get_cl(x))

