from __future__ import division
from sklearn import tree
import Data
import math
import DecisionTree
import SVM
import pandas as pd
import numpy as np
import Plotting
import  matplotlib.pyplot  as plt

#define global variable
data = Data.original_data()
data=data[data.year != 1998]
X = data[['nswprice', 'nswdemand', 'class_data','class','rollingAve','minute',  'month',  'quarter',  'week','weekday']]
Pi_list = []
Si_list = []
accurancy_list = []
Tr_list=[]
Fr_list=[]
error_rate_list=[]

svm_accurancy_list = []
svm_Tr_list=[]
svm_Fr_list=[]
z_list=[]
svm_error_rate_list=[]



global clf
global svm_clf



def drift_detection():

    global clf
    global svm_clf

    #our drift detection includes the week feature 
    # small window use for training the  model
    first_instance = X.iloc[:336]
    next_instance =X.iloc[336:]

    # big wndow use for training the  model
    first_instance2 = X.iloc[:1444]
    next_instance2 = X.iloc[1445:]

    clf,svm_clf = training_model(first_instance)

    #big window
    window_test_model(next_instance2,first_instance2,"Big window")
    #small window
    window_test_model(next_instance,first_instance,"small window")

# method to call decision tree model
def train_decision_model(instance):
    clf = DecisionTree.DecisionTree_Train(instance)
    return clf


# method to call svm  model
def train_svm_model(instance):
    svm_clf = SVM.SVM_Train(instance)
    return svm_clf


def twoSampZ(data,test,window_size):
    from scipy.stats import norm
    import numpy as np
    from numpy import sqrt, abs, round
    std_diff = np.std(data) - np.std(test) / np.std(data)
    SE = np.std(data) / np.sqrt(window_size)
    z_score = np.mean(test) - np.mean(data) / SE
    pval = 2 * (1 - norm.cdf(abs(z_score)))
    return z_score,pval

# training model
def training_model(instance):

    clf = train_decision_model(instance)
    svm_clf = train_svm_model(instance)

    return clf,svm_clf


def window_test_model(next_instance, first_instance,windowName):
    global Pi_list, Si_list,clf,starting_point,svm_clf,z_list

    z_list.append(-200.5)


    for i in range(1,len(next_instance),200):
        new_instance = next_instance.iloc[i]
        # add more instance and test
        first_instance = first_instance.append(new_instance, ignore_index=True)
        first_instance1 = first_instance[['rollingAve']]
        new_instance1 = new_instance[['rollingAve']]
        #calculate z score using only the rolling average
        z = twoSampZ(first_instance1, new_instance1, len(new_instance1))
        z_list
        z_list.append(z)



        if(z>min(z_list)):
            accurancy, error_rate, Tr, Fr = DecisionTree.DecisionTree_Predict(first_instance, clf)
            svm_accurancy, svm_error_rate, svm_Tr, svm_Fr = SVM.SVM_Predict(first_instance, svm_clf)
            accurancy_list.append(accurancy)
            svm_accurancy_list.append(svm_accurancy)
            Tr_list.append(Tr)
            Fr_list.append(Fr)
            svm_Tr_list.append(svm_Tr)
            svm_Fr_list.append(svm_Fr)
            error_rate_list.append(error_rate)
            svm_error_rate_list.append(svm_error_rate)
            print(error_rate)
            first_instance=first_instance.drop(first_instance.index[1])
            print(svm_error_rate)
            clf,svm_clf = training_model(first_instance)
        else:

            del Pi_list[:]
            del Si_list[:]
            del z_list[:]

            first_instance = first_instance.drop(first_instance.index[0:])  # reset instance
            new_first_instance = X.iloc[i:i + 336]

            clf, svm_clf = training_model(new_first_instance)
            print len(X.index[(len(new_first_instance)):])
            print len(new_first_instance)

            window_test_model(new_first_instance, X.iloc[(len(new_first_instance) - 336):],windowName)




    print "accurancy", Tr_list
    print "error rate", Fr_list


    plt.title('Drift decision for decision tree Error rate using '+ windowName)
    Plotting.plot_error_rate(accurancy_list, error_rate_list)
    plt.title('Drift decision for SVM Error rate using '+ windowName)
    Plotting.plot_error_rate(svm_accurancy_list, svm_error_rate_list)








