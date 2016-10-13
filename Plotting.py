
import matplotlib.pylab as plt
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
    plt.show()

    ## plot NSW prce and demand for all data set
def all_data_plot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.legend(fontsize=10, loc='best')
    plt.title('NSW Demand and NSW Price Full Year')
    plt.show()



def monthPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.legend(fontsize=10, loc='best')
    plt.title('NSW Demand and NSW Price Full 1 month')
    plt.show()

def weekPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.title('NSW Demand and NSW Price 1 week')
    plt.legend(fontsize=10, loc='best')
    plt.show()

def dayPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.title('NSW Demand and NSW Price 1 day')
    plt.legend(fontsize=10, loc='best')
    plt.show()

def plotRollAve(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.plot(data['new_date'],  data['rollingAve'], 'green', label="Rolling Ave")
    plt.title('NSW Demand, Rolling Average Price and NSW Price Full Year')
    plt.legend(fontsize=10, loc='best')
    plt.show()

##correlation plot
def corr_plot(df):
    from matplotlib import cm as cm
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cmp = cm.get_cmap('jet',30)
    cax = ax.imshow(df.corr(),interpolation="nearest",cmap=cmp)
    ax.grid(True)
    plt.title("correlation plot of Eletricty data set (incuding new features)")
    labels=['nswprice', 'nswdemand', 'rollingAve']
    ax.set_xticklabels(labels,fontsize=10)
    ax.set_yticklabels(labels, fontsize=10)

    plt.show()


def histograms_seasons(winter, spring, summer, fall, year, month, yr96, yr97, yr98):
    plt.hist(winter['nswprice'],50, normed=1, facecolor='g')
    plt.title("Winter Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(spring['nswprice'],50, normed=1, facecolor='g')
    plt.title("Spring Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(summer['nswprice'],50, normed=1, facecolor='g')
    plt.title("Summer Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(fall['nswprice'],50, normed=1, facecolor='g')
    plt.title("Fall Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(year['nswprice'],50, normed=1, facecolor='g')
    plt.title("NSW Price 1996 to 1998 Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(month['nswprice'], 50, normed=1, facecolor='g')
    plt.title("May 1996 Histogram")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")

    plt.show()

    plt.hist(yr96['nswprice'], 50, normed=1, facecolor='g')
    plt.title("1996")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(yr97['nswprice'], 50, normed=1, facecolor='g')
    plt.title("1997")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")
    plt.show()

    plt.hist(yr98['nswprice'], 50, normed=1, facecolor='g')
    plt.title("1998")
    plt.xlabel("price")
    plt.axis([0, 0.4, 0, 18])
    plt.ylabel("frequency")

    plt.show()