import SVM
import DecisionTree
import Data

def Main():
    data = Data.Train_data()
    train = data[data.year != 1998]
    test = data[data.year == 1998]

    #base line decision tree and SVM
    SVM.SVM_Classifier(train,test)

    DecisionTree.DecisionTree(train,test)

Main()