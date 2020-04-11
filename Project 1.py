#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# read the csv into the dataframe
df = pd.read_csv('arrivals.csv')


# In[5]:


# calculate the Delayed Flights Percentage for Alaska
df.alaska_delayed.sum()/(df.alaska_on_time.sum() + df.alaska_delayed.sum())*100


# In[6]:


# calculate the Delayed Flights Percentage for AM West
df.amwest_delayed.sum()/(df.amwest_on_time.sum() + df.amwest_delayed.sum())*100


# In[7]:


# create a series to hold the delay percentages
alaska_delay_percent = pd.Series(df.alaska_delayed/(df.alaska_on_time + df.alaska_delayed)*100)
alaska_delay_percent


# In[8]:


amwest_delay_percent = pd.Series(df.amwest_delayed/(df.amwest_on_time + df.amwest_delayed)*100)
amwest_delay_percent


# In[10]:


df['alaska_delay_percent'] = alaska_delay_percent
df['amwest_delay_percent'] = amwest_delay_percent
df


# In[11]:


# Plot the delayed flight percentages in each city for each carrier.
df.plot(x='city',y=['alaska_delay_percent','amwest_delay_percent'])


# In[ ]:




