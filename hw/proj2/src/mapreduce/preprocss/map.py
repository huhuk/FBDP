#!/usr/bin/python3

import sys
import re
import jieba
jieba.initialize()

HOME = '/home/huhu/workspace/test/'
stop_file = HOME + 'stopwords.txt'
stop_words = set()
with open(stop_file, 'r') as f:
    for line in f:
        stop_words.add(line.strip())

def get_text(text):
    text = re.sub("[^\u4e00-\u9fa5]+", " ", text)
    text = ' '.join([ i for i in jieba.cut(text) if not i.isspace() and i not in stop_words])
    return text

for line in sys.stdin:
    line = line.strip().split(' ', 1)
    print(line[0], get_text(line[1]))

