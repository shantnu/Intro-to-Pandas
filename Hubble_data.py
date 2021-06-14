#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv("hubble_data.csv")
data.head()


# In[3]:


headers = ["dist","rec_vel"]

data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names = headers)

data_no_headers.head()


# In[4]:


data_no_headers["dist"]


# In[5]:


data.set_index("distance", inplace= True)


# In[6]:


print(data.head())
