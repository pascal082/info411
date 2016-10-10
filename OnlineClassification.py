from __future__ import division
from sklearn import tree
import Data
import math
import DecisionTree
import SVM
import pandas as pd
import  matplotlib.pyplot  as plt
import Plotting



#define global variable
data = Data.original_data()
data = data[['nswprice', 'nswdemand', 'class_data','class', 'rollingAve','year']]
first_half = data[data.year != 1998]
next_half = data[data.year == 1998]



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



def Online_classification():

    global clf
    global svm_clf
    clf,svm_clf = training_model(first_half)

    test_model(next_half)

# method to call decision tree model
def train_decision_model(instance):
    clf = DecisionTree.DecisionTree_Train(instance)
    return clf


# method to call svm  model
def train_svm_model(instance):
    svm_clf = SVM.SVM_Train(instance)
    return svm_clf




# training  model
def training_model(instance):

    clf = train_decision_model(instance)
    svm_clf = train_svm_model(instance)

    return clf,svm_clf



def test_model(instance):
    global clf
    global svm_clf
    print(len(instance))
    #1interval
    for i in range(1, len(instance), 1):
        accurancy, error_rate, Tr, Fr = DecisionTree.DecisionTree_Predict(instance[i], clf)
        svm_accurancy, svm_error_rate, svm_Tr, svm_Fr = SVM.SVM_Predict(instance[i], svm_clf)
        accurancy_list.append(accurancy)
        svm_accurancy_list.append(svm_accurancy)
        Tr_list.append(Tr)
        Fr_list.append(Fr)
        svm_Tr_list.append(svm_Tr)
        svm_Fr_list.append(svm_Fr)
        error_rate_list.append(error_rate)
        svm_error_rate_list.append(svm_error_rate)
        print svm_error_rate
    plt.title('Receiver operating curve for Online classification for SVM/Decision Tree ')
    Plotting.plot_error_rate(svm_accurancy_list, svm_error_rate_list)
    Plotting.plot_error_rate(accurancy_list, error_rate_list)
