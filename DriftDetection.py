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



    for i in range(0, 1200, 48):

        df=X[i:i+48]
        data_label.append(df['class_data'])

        if(df.groupby('class_data').size()[0] >0):

            pi= df.groupby('class_data').size()[0]/(i+48)

            Si= float(math.sqrt(pi*(1 - pi) / i))

            Pi_total.append(pi)

            Si_data.append(Si)

            if( (pi + Si) > (min(Pi_total) + min(Si_data)) ):

                DecisionTree.DecisionTree(df[:2], df[2:])
            else:
                df.drop(df.index, inplace=True)
                #df.drop(df.index[[1,3,5,7]])


drift_detection()
