import  matplotlib.pyplot  as plt

def plot_roc(Tr,Fr,sv_Tr,sv_Fr):
    color = ['#97F0AA', 'g', 'm', 'k', '#E24A33', 'b', 'y', '#001C7F', '#348ABD']

    plt.plot(Fr,Tr, linewidth=2, label='Roc curve when using Decision tree' )
    plt.plot(sv_Fr, sv_Tr,  linewidth=2, label='Roc curve when using SVM')

    plt.ylabel('true positive rate')
    plt.xlabel('false positive rate')


    x = [-0.5, 1.0]
    plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.05)
    plt.legend(fontsize=10, loc='best')
    plt.show()


def  plot_error_rate(accurancy_list, error_rate_list):

    plt.plot(error_rate_list)
    plt._show()