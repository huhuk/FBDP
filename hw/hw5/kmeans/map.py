#!/usr/bin/python3

import sys

cls = list()

def dist(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

def find_cl(x, y):
    res = None
    min_d = -1
    for i in cls:
        now_d = dist(i[1], i[2], x, y)
        if res == None or now_d < min_d:
            min_d = now_d
            res = i[0]
    return res

def emit(cli, x, y):
    print(cli, x, y, sep='\t')

def main():
    for line in sys.stdin:
        x, y = ( float(i) for i in line.strip().split())
        emit(find_cl(x, y), x, y)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            for i in f:
                cl = i.strip().split()[:-1]
                for i in range(1,3):
                    cl[i] = float(cl[i])
                cls.append(cl)

    main()

