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

sv_label=[]
dt_label=[]
dt_accurancy_list=[]

sv_accurancy_list = []
dt_error_list=[]
sv_error_list=[]
svm_error_rate_list=[]

global clf
global svm_clf



def Online_classification():

    global clf
    global svm_clf
    clf,svm_clf = training_model(first_half)
    next_half_labe1 = next_half['class_data']
    test_model(next_half,next_half_labe1)

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



def test_model(instance,label):
    global clf
    global svm_clf
    print(len(instance))
    #1interval
    for i in range(1, len(instance), 1):
        value = DecisionTree.DecisionTree_Predict_Instance(instance[i:i+1], clf)
        dt_label.append(value)
        dt_accurancy, dt_error = calculate_Fpr_Tpr(dt_label, label)
        print dt_accurancy

        svm_value = SVM.SVM_Predict_Instance(instance[i:i+1], svm_clf)
        sv_label.append(svm_value)
        sv_accurancy, sv_error = calculate_Fpr_Tpr(sv_label, label)
        print sv_accurancy
        dt_accurancy_list.append(dt_accurancy)
        sv_accurancy_list.append(sv_accurancy)
        dt_error_list.append(dt_error)
        sv_error_list.append(sv_error)
    plt.title('Receiver operating curve for Online classification for SVM/Decision Tree ')
    Plotting.plot_error_rate(sv_accurancy_list, sv_error_list)
    Plotting.plot_error_rate(dt_accurancy_list, dt_error_list)

def calculate_Fpr_Tpr(value,Y1):
    Tr_list = []
    Fr_list = []
    # count how many was truly positive
    TP = len([i for i, j in zip(Y1, value) if i == j and j == 1])

    # count how many was false positive  i.e incorrectly indentified
    FP = len([i for i, j in zip(Y1, value) if i != j and j == 1])

    # count how many was true negative  i.e correctly rejected
    TN = len([i for i, j in zip(Y1, value) if i != 1 and j == 0])

    # count how many was false negative  i.e incorrectly rejected
    FN = len([i for i, j in zip(Y1, value) if i == 1 and j == 0])

    accurancy = (TP + TN) / len(value)
    error_rate = (TN + FN) / len(value)



    return accurancy,error_rate