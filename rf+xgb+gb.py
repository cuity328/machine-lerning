# -*- coding: utf-8 -*-
"""
Created on Sat Dec 01 21:42:34 2018

@author: tianyu cui
"""

from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

train=pd.read_csv('D:/finaltrain.csv')
test=pd.read_csv('D:/finaltest.csv')
y_train=train['spread5y']
x_train=train.drop('spread5y',axis = 1)
y_test=test['spread5y']
x_test=test.drop('spread5y',axis = 1)

#use randomforest to pick top 50 features
reg=RandomForestRegressor(n_estimators = 50)
reg.fit(x_train,y_train)
importance=list(regr.feature_importances_)
importance=pd.Series(importance)

#combine the values with variables
fea=x_train.assign(importance=importance.values) 
fea_50=fea.sort_values('importance',ascending=False)[0:50]
fea_50=fea_50.drop('importance',axis=1)
xtrain=x_train[list(fea_50)]
xtest=x_test[list(fea_50)]

reg1=RandomForestRegressor(n_estimators = 100,max_depth = 3)
reg1.fit(xtrain,y_train)
pred1=reg1.predict(xtest)

reg2=RandomForestRegressor(n_estimators = 200,max_depth = 3)
reg2.fit(xtrain,y_train)
pred2=reg2.predict(xtest)

reg3=RandomForestRegressor(n_estimators = 500,max_depth = 3)
reg3.fit(xtrain,y_train)
pred3=reg3.predict(xtest)

reg4=RandomForestRegressor(n_estimators = 1000,max_depth = 3)
reg4.fit(xtrain,y_train)
pred4=reg4.predict(xtest)

gbr1=ensemble.GradientBoostingRegressor(n_estimators = 100, max_depth = 3)
gbr1.fit(xtrain, y_train)
pred5=gbr1.predict(xtest)

gbr2=ensemble.GradientBoostingRegressor(n_estimators = 200, max_depth = 3)
gbr2.fit(xtrain, y_train)
pred6=gbr2.predict(xtest)

gbr3=ensemble.GradientBoostingRegressor(n_estimators = 500, max_depth = 3)
gbr3.fit(xtrain, y_train)
pred7=gbr3.predict(xtest)

gbr4=ensemble.GradientBoostingRegressor(n_estimators = 1000, max_depth = 3)
gbr4.fit(xtrain, y_train)
pred8=gbr4.predict(xtest)

xgb1=xgboost.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
xgb1.fit(xtrain, y_train)
pred9=xgb1.predict(xtest)

xgb2=xgboost.XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=3)
xgb2.fit(xtrain, y_train)
pred10=xgb2.predict(xtest)

xgb3=xgboost.XGBRegressor(n_estimators=500, learning_rate=0.1, max_depth=3)
xgb3.fit(xtrain, y_train)
pred11=xgb3.predict(xtest)

xgb4=xgboost.XGBRegressor(n_estimators=1000, learning_rate=0.1, max_depth=3)
xgb4.fit(xtrain, y_train)
pred12=xgb4.predict(xtest)