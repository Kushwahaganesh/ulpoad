#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import *
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor


# In[2]:


df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst


# In[3]:


d1=df['manufacturer'].value_counts()
w=d1[d1.values<10].index
q=list(w)

for i in q:
    w=df[df['manufacturer']==i].index
    for j in list(w):
      df.drop(j,inplace=True)


# In[4]:


df['years_old']=2023-df['year']
df['years_old']
df.drop(columns=['name','year'],axis=1,inplace=True)
df.drop_duplicates(inplace=True)


# In[5]:


df=pd.get_dummies(data=df,columns=['fuel','seller_type','owner','transmission','manufacturer'])

#separating dependent and independent variable


# In[6]:


x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']


# In[7]:


rf=RandomForestRegressor(max_depth=30,n_estimators=20,random_state=35)
rf.fit(x,y)

bg=BaggingRegressor(base_estimator=rf,n_estimators=5,random_state=25)
bg.fit(x,y)

adrf=AdaBoostRegressor(base_estimator=rf,n_estimators=5)
adrf.fit(x,y)

addt=AdaBoostRegressor(base_estimator=DecisionTreeRegressor(max_depth=30),)
addt.fit(x,y)


# In[8]:


import pickle
pickle.dump(adrf,open('adaboost.pkl','wb'))
pickle.dump(rf,open('randomforest.pkl','wb'))
pickle.dump(bg,open('bagging.pkl','wb'))
pickle.dump(addt,open('adadt.pkl','wb'))


# In[ ]:




