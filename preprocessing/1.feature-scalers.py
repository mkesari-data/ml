# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:26:00 2018

@author: mohan
"""

from sklearn import preprocessing
import pandas as pd



df1 = pd.DataFrame({'c1':[1000,900,890,800,700], 'c2':[50,49,48,47,46]})
scaler1 = preprocessing.StandardScaler()
scaler1.fit(df1)
print(scaler1.mean_)
print(scaler1.var_)
out1 = scaler1.transform(df1)
dataset = pd.DataFrame({'C1':out1[:,0],'C2':out1[:,1]})


df2 = pd.DataFrame({'c1':[120,150,200,40,3], 'c2':[250,1,4,230,46]})
scaler2 = preprocessing.MinMaxScaler()
scaler2.fit(df2)
print(scaler2.data_max_)
print(scaler2.data_min_)
out2 = scaler2.transform(df2)
out2

