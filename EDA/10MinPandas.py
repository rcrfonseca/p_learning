#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: raphaelfonseca
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating data structure series
s = pd.Series([1,3,5,np.nan,6,8])
s

#a range of data between days
dates = pd.date_range('20130101',periods=10)
dates

"""
dataframe to insert dates generated before as index
values sorted by numpy for 4 columns

function randn(lines,columns)
"""
df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list('ABCD'))
df

"""
another dataframe 
"""
df2 = pd.DataFrame({
        'A' : 1.,
        'B' : pd.Timestamp('20130102'),
        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
        'D' : np.array([3] * 4,dtype='int32'),
        'E' : pd.Categorical(["test","train","test","train"]),
        'F' : 'foo' })
df2
df2.dtypes

#============================================================

"""
viewing data

head shows first 5 lines
tail shows last 5 lines
both can be customized to show amount of lines
"""

df.head()
df.head(4)
df.tail()
df.tail(3)

"""
functions to better understanding of dataframes
"""
df.index
df.columns
df.values

"""
to describe basic statistcs of dataframes
"""
df.describe()

"""
transpose data
"""
df.T

"""
sorting by axis and values
"""
df.sort_index(axis=0,ascending=True)
df.sort_values(by='B',ascending=False)

