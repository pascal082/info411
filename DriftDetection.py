from __future__ import division
from sklearn import tree
import Data
import math
import DecisionTree
import pandas as pd

def drift_detection():

    data = Data.Train_data()
    X = data[['nswprice', 'nswdemand','class_data']]

    data_set =[]
    data_label=[]
    Pi_total=[]
    Si_data=[]
    df = pd.DataFrame(columns=('nswprice','nswdemand','class_data'))

    #use for taining first time the  model
    first_instance= X.iloc[:24]

    #pass the first 48 data our desciontree and SVM
    clf= DecisionTree.DecisionTree_Train(first_instance)
    pi_model= (first_instance['class_data']==0).sum()/len(first_instance)
    Si_model = float(math.sqrt(pi_model * (1 - pi_model) / pi_model))
    print pi_model, Si_model
    Pi_total.append(pi_model)
    Si_data.append(Si_model)
    accurancy_list=[]

    #set
    train_new_model=0

    for i in range(24, 1000, 1):

        new_instance=X.iloc[:i]
        #first time
        if(len(first_instance)>0 and train_new_model==0):
            instance = X.iloc[:i]
            instance = instance.append(first_instance, ignore_index=True)
        elif(len(first_instance)==0 ):
            print "before appending new instance", len(instance)
            instance = instance.append(new_instance, ignore_index=True)
            print "new instancess", len(instance)


        data_label.append(df['class_data'])



        pi_new= (instance['class_data']==0).sum()/len(instance)


        Si_new= float(math.sqrt(pi_new*(1 - pi_new) / pi_new))
        print pi_new,Si_new, (instance['class_data']==0).sum(),len(instance),Pi_total,Si_model

        if( (pi_new + Si_new) < (min(Pi_total) + min(Si_data)) ):
            accurance=DecisionTree.DecisionTree_Predict(instance,clf)
            accurancy_list.append(accurance)
            print accurancy_list

            clf=DecisionTree.DecisionTree_Train(instance)
            Pi_total.append(pi_new)
            Si_data.append(Si_new)
            if (len(first_instance) > 0):
                first_instance = first_instance.drop(first_instance.index[0:])
            train_new_model=0
        else:
            train_new_model =1
            Pi_total=[]
            Si_data=[]
            instance = instance.drop(instance.index[0:])
            if(len(first_instance)>0):
                first_instance = first_instance.drop(first_instance.index[0:])
            print "drop", len(instance)
            instance = X.iloc[i:i+24]
            print "new",len(instance)
            clf = DecisionTree.DecisionTree_Train(instance)
            pi_new = (instance['class_data']==0).sum() / len(instance)
            Si_new = float(math.sqrt(pi_new * (1 - pi_new) / pi_new))
            #append new pi and si
            Pi_total.append(pi_new)
            Si_data.append(Si_new)
            #print "else instance", len(instance)
            #df.drop(df.index[[1,3,5,7]])


drift_detection()
