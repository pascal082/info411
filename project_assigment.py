#import library
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import datetime
from datetime import timedelta
import os
rcParams['figure.figsize'] = 15, 6

print os.getenv('COMPUTERNAME', 'defaultValue')
#pascal pc
if(os.getenv('COMPUTERNAME', 'defaultValue') =="WKS"):
    data = pd.read_csv(r'C:\Users\pascal\Documents\DataScience\411\elecNorm.csv',index_col='day')
elif(os.getenv('COMPUTERNAME', 'defaultValue') =="RAYMUND"):  #raymund pc
    data = pd.read_csv(r'C:\Users\Raymund\Documents\1_2SEM_MS\INFO411\ASS@\elecNorm.csv', index_col='day')

#add date time column
list=[]
dt_obj = datetime.datetime.strptime("1996-05-06 23:30:00", "%Y-%m-%d %H:%M:%S")
for i in range(len(data)):
    dt_obj +=timedelta(minutes=30)
    list.append(dt_obj)

series2 = pd.Series(list)

data['new_date'] =series2.values


#split date time column day,week,time
column_1 = data['new_date']

datescolumn= pd.DataFrame({"year": column_1.dt.year,
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

newlist=[]
newlist= pd.Series(data['new_date'].values)
datescolumn['new_date']=newlist.values


merge_data= pd.merge(data,datescolumn, on='new_date')

#season
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

merge_data['season'] =season




mean_average=[]

#print np.mean(merge_data['nswprice'][1:48])
for j in range(len(merge_data['nswprice'])):
    mean_average.append(np.mean(merge_data['nswprice'][1:j]))









