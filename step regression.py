# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:39:56 2018

@author: tianyu cui
"""

import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
data=pd.read_csv('D:/ML/compustat_annual_2000_2017_with link information.csv')

#cleaning data
data1=data.dropna(thresh=108683*0.3,axis=1)
data2=data1._get_numeric_data()
data3=data2.fillna(data.median())
data3

#select column "oiadp" as dependent value 
Y=data3['oiadp']
X=data3.loc[:,data3.columns!='oiadp']

#select train set and test set
seed=np.random.rand(len(data3)) < 0.8
Y_train=Y[seed]
X_train=X[seed]
Y_test=Y[~seed]
X_test=X[~seed]
#define a function to step regression

def step_regression(X,Y,p_in=0.05,p_out=0.05):
    #creat two set to store the variables
    Xin=[]
    while True:
        Xout=list(set(X.columns)-set(Xin))
        pvalue=pd.Series(index=Xout)
        for x in Xout:
            lm=sm.OLS(Y,sm.add_constant(pd.DataFrame(X[Xin+[x]]))).fit()
            pvalue[x]=lm.pvalues[x]
        min_pvalue=pvalue.min()
        if min_pvalue<p_in:
            Xin.append(pvalue.idxmin())
        else:
            break
        lm=sm.OLS(Y,sm.add_constant(pd.DataFrame(X[Xin]))).fit()
        pvalue=lm.pvalues.iloc[1:]
        max_pvalue=pvalue.max()
        if max_pvalue>0.05:
            Xin.remove(pvalue.idxmax())
    return Xin
print 'select features are:',step_regression(X_train,Y_train)  
           
            

    
    



