
# In[410]:


c1 = train.filter(lambda x: x[0] == '1 ')
n1 = c1.count()
n1


# In[412]:


c2 = train.filter(lambda x: x[0] == '2 ')
n2 = c2.count()
n2


# In[413]:


c3 = train.filter(lambda x: x[0] == '3 ')
n3 = c3.count()
n3


# In[417]:


tr1 = train.filter(lambda x: x[0] == '1 ')
tr2 = train.filter(lambda x: x[0] == '2 ')
tr3 = train.filter(lambda x: x[0] == '3 ')
ts1 = test.filter(lambda x: x[0] == '1 ')
ts2 = test.filter(lambda x: x[0] == '2 ')
ts3 = test.filter(lambda x: x[0] == '3 ')


# In[462]:


tmp = CountVectorizer(min_df=1)
tr1_x = tmp.fit_transform(tr1.map(lambda x: x[1]).collect())
ts1_x = tmp.transform(ts1.map(lambda x: x[1]).collect())


# In[469]:


a = tr1_x.sum(axis=0)
dump(a, HOME + 'pos.model')
dump(ts1_x, HOME + 'pos.test')


# In[470]:


tmp = CountVectorizer(min_df=1)
tr2_x = tmp.fit_transform(tr2.map(lambda x: x[1]).collect())
ts2_x = tmp.transform(ts2.map(lambda x: x[1]).collect())
a = tr2_x.sum(axis=0)
dump(a, HOME + 'neu.model')
dump(ts2_x, HOME + 'neu.test')


# In[471]:


tmp = CountVectorizer(min_df=1)
tr3_x = tmp.fit_transform(tr3.map(lambda x: x[1]).collect())
ts3_x = tmp.transform(ts3.map(lambda x: x[1]).collect())
a = tr3_x.sum(axis=0)
dump(a, HOME + 'neg.model')
dump(ts3_x, HOME + 'neg.test')

(ts3_x[0] * sp.sparse.csr_matrix(tr3_x.sum(axis=0)).transpose()).data
(ts2_x[0] * sp.sparse.csr_matrix(tr2_x.sum(axis=0)).transpose()).data
(ts1_x[0] * sp.sparse.csr_matrix(tr1_x.sum(axis=0)).transpose()).data
