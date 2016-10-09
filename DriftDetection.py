from __future__ import division
from sklearn import tree
import Data
import math
import DecisionTree
import SVM
import pandas as pd
import Ploting
import  matplotlib.pyplot  as plt

#define global variable
data = Data.Train_data()
X = data[['nswprice', 'nswdemand', 'class_data','class']]
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

drift_change = 0
global clf
global svm_clf
starting_point=1


def drift_detection():
    # use for taining first time the  model
    first_instance = X.iloc[:336]

    global clf
    global svm_clf
    clf,svm_clf = training_model(first_instance)

    test_model(first_instance,X)

# method to call decision tree model
def train_decision_model(instance):
    clf = DecisionTree.DecisionTree_Train(instance)
    return clf


# method to call svm  model
def train_svm_model(instance):
    svm_clf = SVM.SVM_Train(instance)
    return svm_clf




# training initial or re-training first model
def training_model(instance):
    global Pi_list,Si_list
    # pass the first/next 48 data to our decisiontree and SVM
    clf = train_decision_model(instance)
    svm_clf = train_svm_model(instance)
    pi_model,Si_model = calculate_pi_si(instance)
    Pi_list.append(pi_model)
    Si_list.append(Si_model)


    return clf,svm_clf


def calculate_pi_si(instance):
    pi_new = (instance['class_data'] == 0).sum() / len(instance)

    Si_new = float(math.sqrt(pi_new * (1 - pi_new) / pi_new))
    return pi_new, Si_new


def update_pi_si_list(pi, si):
    Pi_list.append(pi)
    Si_list.append(si)
    return Pi_list, Si_list


def detect_drift(pi, si):
    global drift_change
    if ((pi + si) < (min(Pi_list) + min(Si_list))):
        drift_change = 0
    else:
        drift_change = 1
    return drift_change


def test_model(first_instance,X):
    global Pi_list, Si_list,clf,starting_point,svm_clf


    for i in range(len(first_instance),len(X),2320):
        new_instance = X.iloc[i:i+2320]
        #for first time to train model only
        if (starting_point==1):
            instance = first_instance.append(new_instance, ignore_index=True)
            #set starting oint to 0 because we would never come back to this point
            starting_point = 0
        else:
            instance = instance.append(new_instance, ignore_index=True)


        pi_new, Si_new = calculate_pi_si(instance)


        if (detect_drift(pi_new, Si_new) == 0):

            accurancy,error_rate,Tr,Fr = DecisionTree.DecisionTree_Predict(instance, clf)
            svm_accurancy, svm_error_rate, svm_Tr, svm_Fr = SVM.SVM_Predict(instance, svm_clf)
            accurancy_list.append(accurancy)
            svm_accurancy_list.append(svm_accurancy)
            Tr_list.append(Tr)
            Fr_list.append(Fr)
            svm_Tr_list.append(svm_Tr)
            svm_Fr_list.append(svm_Fr)
            error_rate_list.append(error_rate)
            svm_error_rate_list.append(svm_error_rate)
            update_pi_si_list(pi_new, Si_new)

            print "Accepting instance"

        else:
            # reset global variable and empty instance
            del Pi_list[:]
            del Si_list[:]

            instance = instance.drop(instance.index[0:])  #reset instance
            instance = X.iloc[i:i + 2320]
            print "droping model"
            print "re-training model"
            clf,svm_clf = training_model(instance)




    print "accurancy", Tr_list
    print "error rate", Fr_list


    plt.title('Decision tree Error rate ')
    Ploting.plot_error_rate(accurancy_list, error_rate_list)
    plt.title('SVM Error rate ')
    Ploting.plot_error_rate(svm_accurancy_list, svm_error_rate_list)

    plt.title('Receiver operating curve for drift detection for SVM/Decision Tree ')
    Ploting.plot_roc(Tr_list, Fr_list, svm_Tr_list, svm_Fr_list)












