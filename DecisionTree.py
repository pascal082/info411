from __future__ import division
from sklearn import tree
import Data

def DecisionTree(train,test):

    X = train[['nswprice', 'nswdemand']]
    Y = train['class_data']
    X1 = test[['nswprice', 'nswdemand']]
    Y1 = test['class_data']

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    TG = []
    FG = []
    Tr = []
    Fr = []

    value = clf.predict(X1)

    # count how many was truly positive
    TP = len([i for i, j in zip(Y1, value) if i == j and j == 1])

    # count how many was false positive  i.e incorrectly indentified
    FP = len([i for i, j in zip(Y1, value) if i != j and j == 1])

    # count how many was true negative  i.e correctly rejected
    TN = len([i for i, j in zip(Y1, value) if i != 1 and j == 0])

    # count how many was false negative  i.e incorrectly rejected
    FN = len([i for i, j in zip(Y1, value) if i == 1 and j == 0])


    accurancy= (TP+TN)/len(value)
    print  'Decision Tree Accuracy:', accurancy * 100


