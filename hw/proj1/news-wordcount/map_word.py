#!/usr/bin/python3

import sys
import jieba

stop_words = set()

def generateLongCountToken(item):
    print(item + "\t" + "1")

def stop_file(filename):
    global stop_words
    with open(filename, 'r') as f:
        for word in f:
            if word.strip():
                stop_words.add(word.strip())

def solve_stop(word):
    if word not in stop_words and not word.isspace():
        generateLongCountToken(word)

def main(argv):
    for line in sys.stdin:
        words = ' '.join(line.split()[4:-1]).strip()
        for word in jieba.cut(words):
            solve_stop(word)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        stop_file(sys.argv[1])
    main(sys.argv)

