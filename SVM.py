from __future__ import division
from sklearn import svm
import Data

#wbaseline classifier frm orig data
def SVM_Classifier(train,test):

    X = train[['nswprice', 'nswdemand']]
    Y = (train['class'] == 'UP').astype(int)
    X1 = test[['nswprice', 'nswdemand']]
    Y1 = (test['class'] == 'UP').astype(int)

    clf = svm.SVC(kernel='linear', C=1.0)
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

    error_rate = (TN + FN) / len(value)

    return accurancy, error_rate


def SVM_Train(train):
    X = train[['nswprice', 'nswdemand', 'rollingAve']]

    Y = (train['class'] == 'UP').astype(int)


    clf = svm.SVC(kernel='linear', C=1.0)
    clf = clf.fit(X, Y)
    return clf


def SVM_Predict(test, clf):
    X1 = test[['nswprice', 'nswdemand', 'rollingAve']]
    Y1 = (test['class'] == 'UP').astype(int)

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

    accurancy = (TP + TN) / len(value)
    error_rate = (TN +FN)/ len(value)
    FPR = float(FP / (TN + FP))
    TPR = float(TP / (TP + FN))
    Tr.append(TPR)
    Fr.append(FPR)


    return accurancy,error_rate,Tr,Fr











