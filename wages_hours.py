#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd



# In[2]:


data = pd.read_csv("wages_hours.csv")
data.head()


# In[3]:


data = pd.read_csv("wages_hours.csv", sep = "\t")
data.head()


# In[4]:


data


# In[5]:


data2 = data[["AGE", "RATE"]]
data2.head()


# In[6]:


data_sorted = data2.sort_values(["AGE"])
data_sorted.head()


# In[7]:


data_sorted.set_index("AGE", inplace=True)
print(data_sorted.head())




# In[ ]:
