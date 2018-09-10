# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:39:56 2018

@author: tianyu cui
"""

import pandas as pd
data=pd.read_csv('D:/ML/compustat_annual_2000_2017_with link information.csv')
data
data=data.dropna(thresh=1614349*0.3,axis=1)
data=data._get_numeric_data()
data=data.fillna(data.median())
data

