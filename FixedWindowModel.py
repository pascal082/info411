from __future__ import division
from sklearn import tree
import Data
import math
import DecisionTree
import SVM
import pandas as pd
import Plotting
import  matplotlib.pyplot  as plt

#define global variable
data = Data.season_summer()
X = data[['nswprice', 'nswdemand', 'class_data','class','rollingAve']]
Pi_list = []
Si_list = []
accurancy_list = []
Tr_list=[]
Fr_list=[]
error_rate_list=[]

svm_accurancy_list = []
svm_Tr_list=[]
svm_Fr_list=[]
svm_error_rate_list=[]



global clf
global svm_clf



def FixedWindowModel():

    global clf
    global svm_clf

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




# training model
def training_model(instance):

    clf = train_decision_model(instance)
    svm_clf = train_svm_model(instance)

    return clf,svm_clf


def window_test_model(next_instance, first_instance,windowName):
    global Pi_list, Si_list,clf,starting_point,svm_clf


    for i in range(1,len(next_instance),1):
        new_instance = next_instance.iloc[i]
        # add more instance and test
        first_instance = first_instance.append(new_instance, ignore_index=True)

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
        print(len(first_instance))
        first_instance=first_instance.drop(first_instance.index[1])
        print(len(first_instance))
        clf,svm_clf = training_model(first_instance)




    print "accurancy", Tr_list
    print "error rate", Fr_list


    plt.title('Decision tree Error rate '+ windowName)
    Plotting.plot_error_rate(accurancy_list, error_rate_list)
    plt.title('SVM Error rate '+ windowName)
    Plotting.plot_error_rate(svm_accurancy_list, svm_error_rate_list)





