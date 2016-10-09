import SVM
import DecisionTree
import Data
import Plots

def Main():
    data = Data.Train_data()
    train = data[data.year != 1998]
    test = data[data.year == 1998]

    #base line decision tree and SVM
    #SVM.SVM_Classifier(train,test)
    #Plots.all_data_plot(Data.original_data())
    #Plots.monthPlot(Data.month5_96())
    #Plots.weekPlot(Data.week_96())
    #Plots.dayPlot(Data.day())
    Plots.plotROllAve(Data.original_data())

    #DecisionTree.DecisionTree(train,test)

Main()