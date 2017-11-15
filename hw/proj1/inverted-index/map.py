#!/usr/bin/python3

import sys
import jieba

stop_words = set()
#filename = os.getenv("mapreduce_map_input_file").split("/")[-1]

def generateToken(items):
    print('\t'.join(items))

def get_stop_words(filename):
    global stop_words
    with open(filename, 'r') as f:
        for word in f:
            stop_words.add(word.strip())

def word_filter(word):
    if word in stop_words or word.isspace():
        return False
    return True

if len(sys.argv) > 1:
    get_stop_words(sys.argv[1])

for line in sys.stdin:
    total = line.strip().split()
    code = total[0]
    name = total[1]
    filename = code + name + '.txt'
    #date = total[2]
    #time = total[3]
    title = ' '.join(total[4:-1])
    url = total[-1]
    for word in set(jieba.cut(title)):
        if word_filter(word):
            generateToken([word, filename, url])


