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

#print merge_data.head(4)
#merge_data.tail()

summer = merge_data[merge_data.season =='summer']

#print summer.head()
#print summer.tail()

plt.plot(summer['new_date'],summer['nswprice'],'blue',label="NSW Summer Price")
plt.plot(summer['new_date'],summer['nswdemand'],'red',label="NSW Summer Demand")
plt.show()