# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:24:39 2018

@author: tianyu cui
"""

import pandas as pd
data1=pd.read_stata('D:/ML/cds_spread5y_2001_2016.dta')
data1
data2=pd.read_stata('D:/ML/crsp_quart.dta')
data2
data=pd.merge(data1,data2,left_on=['gvkey','mdate'],right_on=['gvkey','datadate'],how='left')
data

for n in range(56556):
    data.iloc[3*n,9:29]=data.iloc[3*n+2,9:29]
    data.iloc[3*n+1,9:29]=data.iloc[3*n+2,9:29]
    
data.dropna(thresh=10,axis=0)

    
    