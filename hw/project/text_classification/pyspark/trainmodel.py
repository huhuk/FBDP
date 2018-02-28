
#========SVM========#  
def SvmClass(x_train, y_train, kernel = 'linear'):
    clf = SVC(kernel = kernel,probability=True)
    clf.fit(x_train, y_train)
    return clf

#========KNN========#  
def KnnClass(x_train, y_train, k = 5):  
    from sklearn.neighbors import KNeighborsClassifier  
    clf=KNeighborsClassifier(k)  
    clf.fit(x_train,y_train)  
    return clf 

#=====NB=========#  
def NbClass(x_train, y_train):  
    from sklearn.naive_bayes import MultinomialNB  
    clf=MultinomialNB(alpha=0.01).fit(x_train, y_train)   
    return clf  

#========Decision Tree ========#  
def DccisionClass(x_train,y_train):  
    from sklearn import tree  
    clf=tree.DecisionTreeClassifier()  
    clf.fit(x_train,y_train)  
    return clf  


