# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 00:47:29 2018

@author: tianyu cui
"""

import pandas as pd
import numpy as np

data=pd.read_csv('D:/ML/compustat_annual_2000_2017_with link information.csv')
len(data)
#cleaning data
data1=pd.DataFrame(columns=list(data))
for x in range (0,len(data)):
    if data.loc[x,'oiadp']!=0:
        data1.append(data.loc[x,])

#select column "oiadp" as dependent value 
Y=data1['oiadp']
X=data3.loc[:,data3.columns!='oiadp']

def GetAllVar(dataSet):
    return var(dataSet[:,-1])*shape(dataSet)[0]

def dataSplit(dataSet,feature,featNumber):
    dataL =  dataSet[nonzero(dataSet[:,feature] > featNumber)[0],:]
    dataR = dataSet[nonzero(dataSet[:,feature] <= featNumber)[0],:]
    return dataL,dataR


def choseBestFeature(dataSet,op = [1,4]):        
    if len(set(dataSet[:,-1].T.tolist()[0]))==1:    
        regLeaf = mean(dataSet[:,-1])         
        return None,regLeaf                   
    Serror = GetAllVar(dataSet)
    BestFeature = -1; BestNumber = 0; lowError = inf
    m,n = shape(dataSet)
    for i in range(n-1):   
        for j in set(dataSet[:,i].T.tolist()[0]):
            dataL,dataR = dataSplit(dataSet,i,j)
            if shape(dataR)[0]<op[1] or shape(dataL)[0]<op[1]: continue  
            tempError = GetAllVar(dataL) + GetAllVar(dataR)
            if tempError < lowError:
                lowError = tempError; BestFeature = i; BestNumber = j
    if Serror - lowError < op[0]:            
        return None,mean(dataSet[:,-1])         
    dataL, dataR = dataSplit(dataSet, BestFeature, BestNumber)
    if shape(dataR)[0] < op[1] or shape(dataL)[0] < op[1]:       
        return None, mean(dataSet[:, -1])
    return BestFeature,BestNumber


def createTree(dataSet,op=[1,4]):
    bestFeat,bestNumber = choseBestFeature(dataSet,op)
    if bestFeat==None: return bestNumber
    regTree = {}
    regTree['spInd'] = bestFeat
    regTree['spVal'] = bestNumber
    dataL,dataR = dataSplit(dataSet,bestFeat,bestNumber)
    regTree['left'] = createTree(dataL,op)
    regTree['right'] = createTree(dataR,op)
    return  regTree

