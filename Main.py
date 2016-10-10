import SVM
import DecisionTree
import Data
import DriftDetection
import OnlineClassification
import  FixedWindowModel
import  matplotlib.pyplot  as plt
import Plotting
import Clustering

def Main():
    data = Data.Train_data()
    train = data[data.year != 1998]
    test = data[data.year == 1998]

    #base line decision tree and SVM
    #accuracy_list, error_rate_list=SVM.SVM_Classifier(train,test)
    #svm_accuracy_list, svm_error_rate_list= DecisionTree.DecisionTree(train,test)

    #print "Decision tree accurance :", accuracy_list
    #print "Decision error rate :", error_rate_list
    #print "SVM accuracy:",svm_accuracy_list
    #print "SVM error rate :", error_rate_list


    #online classification for Decision tree and SVM
    #OnlineClassification.Online_classification()

    #drift detection svm and decision tree
    #DriftDetection.drift_detection()

    #small and big window detection
    #FixedWindowModel.FixedWindowModel()

    # SVM.SVM_Classifier(train,test)
    #Plotting.all_data_plot(Data.original_data())
    #Plotting.monthPlot(Data.month5_96())
    #Plotting.weekPlot(Data.week_96())
    #Plotting.dayPlot(Data.day())
    #Plotting.plotRollAve(Data.original_data())
    Clustering.Clusters(Data.kdata())




Main()