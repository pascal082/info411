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

    ##full year performance
    #data = Data.Train_data()
    #train = data[data.year != 1998]
    #test = data[data.year == 1998]



    #base line decision tree and SVM
    #svm_accuracy_list, svm_error_rate_list=SVM.SVM_Classifier(train,test)
    #accuracy_list, error_rate_list= DecisionTree.DecisionTree(train,test)

    #print "Decision tree accuracy :", accuracy_list
    #print "Decision error rate :", error_rate_list
    #print "SVM accuracy:",svm_accuracy_list
    #print "SVM error rate :", error_rate_list

    ##Spring season perf performance
    #data = Data.season_spring()
    #train = data[data.year != 1998]
    #test = data[data.year == 1998]

    #Spring baseline decision tree and SVM
    #svm_accuracy_list, svm_error_rate_list = SVM.SVM_Classifier(train, test)
    #accuracy_list, error_rate_list = DecisionTree.DecisionTree(train, test)
    #print "Spring base line performance"
    #print "Decision tree accuracy :", accuracy_list
    #print "Decision error rate :", error_rate_list
    #print "SVM accuracy:", svm_accuracy_list
    #print "SVM error rate :", error_rate_list

    ##summer season perf performance
    #data = Data.season_summer()
    #train = data[data.year != 1998]
    #test = data[data.year == 1998]

    # summer baseline decision tree and SVM
    #svm_accuracy_list, svm_error_rate_list = SVM.SVM_Classifier(train, test)
    #accuracy_list, error_rate_list = DecisionTree.DecisionTree(train, test)
    #print "Summer base line performance"
    #print "Decision tree accuracy :", accuracy_list
    #print "Decision error rate :", error_rate_list
    #print "SVM accuracy:", svm_accuracy_list
    #print "SVM error rate :", error_rate_list

    ##winter season perf performance
    #data = Data.season_winter()
    #train = data[data.year != 1998]
    #test = data[data.year == 1998]

    # WInter baseline decision tree and SVM
    #svm_accuracy_list, svm_error_rate_list = SVM.SVM_Classifier(train, test)
    #accuracy_list, error_rate_list = DecisionTree.DecisionTree(train, test)
    #print "Winter base line performance"
    #print "Decision tree accuracy :", accuracy_list
    #print "Decision error rate :", error_rate_list
    #print "SVM accuracy:", svm_accuracy_list
    #print "SVM error rate :", error_rate_list
"""
    #fall season perf performance
    data = Data.season_autumn()
    train = data[data.year != 1998]
    test = data[data.year == 1998]

    # Fall baseline decision tree and SVM
    svm_accuracy_list, svm_error_rate_list = SVM.SVM_Classifier(train, test)
    accuracy_list, error_rate_list = DecisionTree.DecisionTree(train, test)
    print "Autumn base line performance"
    print "Decision tree accuracy :", accuracy_list
    print "Decision error rate :", error_rate_list
    print "SVM accuracy:", svm_accuracy_list
    print "SVM error rate :", error_rate_list
    #online classification for Decision tree and SVM
    #OnlineClassification.Online_classification()
"""
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
    #Clustering.Clusters(Data.kdata())




Main()