
import pyspark
import numpy as np
import scipy as sp
from preprocess import *
from trainmodel import *

sc = pyspark.SparkContext(appName='preprocess')

text = sc.textFile('file:///home/huhu/workspace/test/raw.txt')

# 划分数据集： 训练集 / 测试集
data = text.map(lambda _: (_[:2], get_text(_[2:])) ).randomSplit((0.7, 0.3))
train, test = data
x_train = train.map(lambda x: x[1]).collect()
y_train = train.map(lambda x: x[0]).collect()

# tfidf 特征提取
count_vec = TfidfVectorizer(binary = False)
x_train = count_vec.fit_transform(x_train)

# svm
svm_clf = SvmClass(x_train, y_train)
ans = np.array(test.map( lambda x: [x[0], int(svm_clf.predict(count_vec.transform( [ x[1] ] ))[0] ) ] ) .collect())
svm_acc = np.mean(ans[:, 0].astype(np.int) == ans[:, 1].astype(np.int))

# knn
knn_clf = KnnClass(x_train, y_train, 3)
ans3 = np.array(test.map( lambda x: [ x[0], int( knn_clf.predict(count_vec.transform( [ x[1] ] ))[0] ) ] ) .collect())
knn_acc = np.mean(ans3[:, 0].astype(np.int) == ans3[:, 1].astype(np.int))

# naive bayes
nb_clf = NbClass(x_train, y_train)
ans4 = np.array(test.map( lambda x: [ x[0], int( nb_clf.predict(count_vec.transform( [ x[1] ] ))[0] ) ] ) .collect())
nb_acc = np.mean(ans4[:, 0].astype(np.int) == ans4[:, 1].astype(np.int))

# decision tree
dc_clf = DccisionClass(x_train, y_train)
ans5 = np.array(test.map( lambda x: [ x[0], int( dc_clf.predict(count_vec.transform( [ x[1] ] ))[0] ) ] ) .collect())
dc_acc = np.mean(ans5[:, 0].astype(np.int) == ans5[:, 1].astype(np.int))

sc.stop()

# dump(x_train, HOME + 'x_train.model')
# dump(y_train, HOME + 'y_train.model')
# test.map(lambda a: a[0] + a[1]).saveAsTextFile('file://' + HOME + 'test')
# a = load(HOME + 'y_train.model')
# b = load(HOME + 'x_train.model')

# dump(count_vec, HOME + 'tfidf.model')
# count_vec2 = load(HOME + 'tfidf.model')

# n = x_train.shape[0]
# one = sp.sparse.csr_matrix(np.ones(n).reshape((n,1)))
# dists = sp.sparse.linalg.norm((x_train - one * t3), axis=1)
