import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import datetime
from datetime import timedelta
import os
from sklearn import tree
import numpy as np
rcParams['figure.figsize'] = 15, 6


def original_data():

    if (os.getenv('COMPUTERNAME', 'defaultValue') == "WKS"):
        data = pd.read_csv(r'C:\Users\pascal\Documents\DataScience\411\elecNorm.csv', index_col='day')
    elif (os.getenv('COMPUTERNAME', 'defaultValue') == "RAYMUND"):  # raymund pc
        data = pd.read_csv(r'C:\Users\Raymund\Documents\1_2SEM_MS\INFO411\ASS@\elecNorm.csv', index_col='day')

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

    # season
    season = []
    for i in merge_data['month']:
        if i == 12 or i == 1 or i == 2:
            season.append('summer')
        elif 3 <= i <= 5:
            season.append('autumn')
        elif 6 <= i <= 8:
            season.append('winter')
        elif 9 <= i <= 11:
            season.append('spring')
        else:
            season.append('none')

    merge_data['season'] = season

    #add new column to take care of up and down
    class_data = []
    for i in merge_data['class']:
        if i == 'UP':
            class_data.append(1)
        elif i == 'DOWN':
            class_data.append(0)
    merge_data['class_data'] = class_data

    return merge_data


# get training data with nswprice and nswdemand as features
def Train_data():
    data=original_data()
    data = data[['nswprice', 'nswdemand','class_data','year','period','class']]
    return data










