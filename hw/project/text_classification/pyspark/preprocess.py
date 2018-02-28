
import re
import jieba
jieba.initialize()

def get_stopwords():
    stop_file = '/home/huhu/data/FBDP/proj1/stopwords.txt'
    stop_words = set()
    with open(stop_file, 'r') as f:
        for line in f:
            stop_words.add(line.strip())
    return stop_words

def get_text(text):
    text = re.sub("[^\u4e00-\u9fa5]+", " ", text)
    text = ' '.join([ i for i in jieba.cut(text) if not i.isspace() and i not in stop_words])
    return text
