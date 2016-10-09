import Data
import matplotlib.pylab as plt

## plot NSW prce and demand for all data set
def all_data_plot(data):
    plt.plot(data['new_date'], data['nswprice'],'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label = 'NSW Demand')
    plt.show()

def monthPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.show()

def weekPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.show()

def dayPlot(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.show()

def plotROllAve(data):
    plt.plot(data['new_date'], data['nswprice'], 'blue', label="NSW Price")
    #plt.plot(data['new_date'], data['nswdemand'], 'red', label='NSW Demand')
    plt.plot (data['new_date'], Data.rollingAve(), 'green', label = "Rolling Ave" )
    plt.show()

