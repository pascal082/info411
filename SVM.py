from __future__ import division
from sklearn import svm
import Data

def SVM_Classifier(train,test):


    #print train.head()
    ## subset training and testing data
    X= train[['nswprice','nswdemand','period']]
    X_test = test[['nswprice','nswdemand','period']]

    #subset target convert to 1 and 0
    y =train[['class_data']]
    y_test =test[['class_data']]
    #plt.scatter(X,Y)
    #plt.show()


    #fit model
    clf = svm.SVC(kernel='rbf', C = 1.0)

    clf.fit(X,y)

    print 'SVC Model:', clf.score(X,y)

    ## use model to predict

    ypred_label = clf.predict(X_test)
    print ypred_label
    ## measure accuracy of SVM
    Tr=[]
    Fr=[]
    # count how many was truly positive
    TP = len([i for i, j in zip(y_test, ypred_label) if i == j and j == 1])

    # count how many was false positive  i.e incorrectly indentified
    FP = len([i for i, j in zip(y_test, ypred_label) if i != j and j == 1])

    # count how many was true negative  i.e correctly rejected
    TN = len([i for i, j in zip(y_test, ypred_label) if i != 1 and j == 0])

    # count how many was false negative  i.e incorrectly rejected
    FN = len([i for i, j in zip(y_test, ypred_label) if i == 1 and j == 0])


    print TP,TN,FP,FN,len(ypred_label)
    accurancy = (TP + TN)/ len(ypred_label)
    print  'SVC Accuracy:', accurancy * 100



