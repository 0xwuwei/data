#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


sample_data = pd.read_csv('sample_data.csv')


# In[5]:


sample_data


# In[7]:


from matplotlib import pyplot as plt


# In[9]:


x = [1,2,3]
y = [7, 12, 24]
plt.plot(x,y)


# In[10]:


type(sample_data)


# In[11]:


sample_data.column_c


# In[13]:


type(sample_data.column_c)


# In[15]:


sample_data.column_c.iloc[1]


# In[18]:


plt.plot(sample_data.column_a, sample_data.column_c)


# In[17]:


sample_data


# In[ ]:




