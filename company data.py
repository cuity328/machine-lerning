# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:57:57 2018

@author: tianyu cui
"""

import pandas as pd
data=pd.read_csv('D:/ML/company data.csv')
print data

#select useful columns 
data2=data.iloc[:,8:23]
print data2
summary=data2.describe()

#clean data
finaldata=data2.dropna(thresh=363542*0.5,axis=1)
finaldata.rename(columns={'atq': 'total asset', 'chq': 'cash', 'dlttq': 'long term debt','lctq':'current liability','niq':'net income','revtq':'total revenue','dvy':'cash dividends'}, inplace=True) 
print finaldata