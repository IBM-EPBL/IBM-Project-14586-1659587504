# -*- coding: utf-8 -*-
"""Copy of Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17jkvOdHAyXOBsrQX0GDqSI-W7phm38mJ
"""

s = "Hi there Shsm!"
s.split()





planet = "jupiter"
diameter = 9087
print("The diameter of {} is {}kilometers".format(planet,diameter))

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'smsh']}]}]}
d['k1'][3]['tricky'][3]['target'][3]

import numpy as np

array=np.zeros(0)
array=np.ones(0)*5

array=np.arange(20,36,2)

np.arange(0,16).reshape((4,4))

a=np.array([1,2,3])
b=np.array([4,5,6])
ab=np.concatenate((a,b),axis=0)
ab

import pandas as pd

data=[['malesh',30],['shiny',15],['juu',12]]
df=pd.DataFrame(data,columns=['Name','Age'])
df

smsh=pd.date_range(start='13-04-2023',end='12-05-2023')
for val in smsh:
  print(val)

lists = [[1, 'sss', 22], [2, 'mmm', 25], [3, 'hhh', 24]]

lists=[[1,'ss',22],[2,'bbb',25],[3,'ccc',24]]
df=pd.DataFrame(lists,columns=['s.no','name','Age'])
print(df)