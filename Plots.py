import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import datetime
from datetime import timedelta


rcParams['figure.figsize'] = 15, 6

## load data set
data = pd.read_csv(r'C:\Users\Raymund\Documents\1_2ndSEM_MS\INFO411\ASS2\elecNorm.csv', index_col='day')

# add date time column
list = []
dt_obj = datetime.datetime.strptime("1996-05-06 23:30:00", "%Y-%m-%d %H:%M:%S")
for i in range(len(data)):
    dt_obj += timedelta(minutes=30)
    list.append(dt_obj)

series2 = pd.Series(list)

data['new_date'] = series2.values

# split date time column day,week,time
column_1 = data['new_date']

datescolumn = pd.DataFrame({"year": column_1.dt.year,
                            "month": column_1.dt.month,
                            "day": column_1.dt.day,
                            "minute": column_1.dt.minute,
                            "hour": column_1.dt.hour,
                            "dayofyear": column_1.dt.dayofyear,
                            "week": column_1.dt.week,
                            "weekofyear": column_1.dt.weekofyear,
                            "dayofweek": column_1.dt.dayofweek,
                            "weekday": column_1.dt.weekday,
                            "quarter": column_1.dt.quarter,

                            })

newlist = []
newlist = pd.Series(data['new_date'].values)
datescolumn['new_date'] = newlist.values

merge_data = pd.merge(data, datescolumn, on='new_date')
merge_data['new_date'] = merge_data.index
#print merge_data
## season column
season=[]
for i in merge_data['month']:
   if i ==12 or i ==1 or i == 2:
       season.append('summer')
   elif 3<=i <=5:
       season.append('autumn')
   elif 6<=i <=8:
       season.append('winter')
   elif 9<=i <=11:
       season.append('spring')
   else:
       season.append('none')

merge_data['season'] = season


#merge_data.tail()

rollingAve = pd.rolling_mean(merge_data['nswprice'], 48)
##merge_data.append(rollingAve);

#print merge_data.head(4)
##plot all demand and price

#print rollingAve


## rolling average
plt.plot(merge_data['new_date'], merge_data['nswprice'],'blue', label="NSW Price")
plt.plot(merge_data['new_date'], rollingAve,'red', label="NSW Demand")
plt.plot(merge_data['new_date'], merge_data['nswdemand'], 'green', label =" NSW Demand")
#plt.show()

#month
#plt.plot(merge_data['new_date'], merge_data['nswprice'],'blue', label="NSW Price")
#plt.plot(merge_data['new_date'], merge_data['nswdemand'],'red', label="NSW Demand")
#plt.show()

##summer
summer = merge_data[merge_data.season =='summer']
winter = merge_data[merge_data.season =='winter']

print len (winter)

winter = winter.drop(winter.index[0:],)
print len (winter)
print merge_data.iloc[[4],]

summer= summer.append(winter, ignore_index = True)
#print "head:" ,summer.head()
#print  "tail:" ,summer.tail()

s1 = summer[summer.season == 'winter']

#print s1.head()
#plt.plot(summer['new_date'],summer['nswprice'],'blue',label="NSW Summer Price")
#plt.plot(summer['new_date'],summer['nswdemand'],'red',label="NSW Summer Demand")
#plt.show()

## plot daily
week1 = merge_data[0:337]

#print week1.head()

#plt.plot(week1['new_date'],week1['nswprice'],'blue',label="NSW Summer Price")
#plt.plot(week1['new_date'],week1['nswdemand'],'red',label="NSW Summer Demand")
#plt.show()


yr1998 = merge_data[merge_data.year == 1998]

month198 = yr1998[yr1998.month == 9]
#plt.plot(month198['new_date'],month198['nswprice'],'blue',label="NSW May 98 Price")
#plt.plot(month198['new_date'],month198['nswdemand'],'red',label="NSW May 98 Demand")
#plt.show()
