#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
import hvplot.pandas


# In[2]:


load_dotenv()


# In[3]:


fred_api_key = os.getenv('FRED_API_KEY')


# In[4]:


type(fred_api_key)


# In[6]:


category_id = 'DEXUSEU'


# In[7]:


url = f'https://api.stlouisfed.org/fred/series/observations?series_id={category_id}&api_key={fred_api_key}&file_type=json'


# In[8]:


data = requests.get(url).json()


# In[9]:


df = pd.DataFrame(data['observations'][-100:-1])


# In[10]:


df.head(25)


# In[11]:


df = df.dropna()


# In[12]:


df = df[df['value'] != '.']


# In[13]:


df.head(20)


# In[14]:


df['value'] = df['value'].astype('float')


# In[15]:


df.dtypes


# In[16]:


df['inverse'] = 1 / df['value']


# In[17]:


df


# In[18]:


df = df[['date', 'value', 'inverse']]


# In[19]:


df


# In[20]:


df = df.set_index('date')


# In[21]:


df


# In[22]:


df.index = pd.to_datetime(df.index)


# In[23]:


df.index


# In[25]:


df = df.rename(columns = {'value' : 'spot rate', 'inverse' : 'inverse rate'})
df


# In[30]:


df.hvplot.line(x='date', y=['spot rate', 'inverse rate'])


# In[35]:


df['SMA10'] = df['spot rate'].rolling(window=10, min_periods = 10).mean()
df = df.dropna()
df


# In[40]:


df.hvplot.line(x = 'date', y = ['spot rate','SMA10'])


# In[62]:


df['ema10'] = df['spot rate'].ewm(span=10).mean()
df['ema20'] = df['spot rate'].ewm(span=20).mean()
df['ema30'] = df['spot rate'].ewm(span=30).mean()
df['ema50'] = df['spot rate'].ewm(span=50).mean()
df['ema100'] = df['spot rate'].ewm(span=100).mean()
df['ema200'] = df['spot rate'].ewm(span=200).mean()
df


# In[61]:


current_spot_rate = df['spot rate'].iloc[-1]
current_SMA10 = df['SMA10'].iloc[-1]
current_EMA10 = df['ema10'].iloc[-1]
current_EMA50 = df['ema50'].iloc[-1]
print(f'Spot Rate = ${current_spot_rate}')
print(f'SMA10 = ${current_SMA10}')
print(f'EMA10 = ${current_EMA10}')
print(f'EMA50 = ${current_EMA50}')


# In[55]:


#buy if avg is greater than rate
#buy is a high count, sell is low coun

def indicator(spot_rate,avg):
    count = 0
    if avg > spot_rate:
        count = 1
    elif avg == spot_rate:
        count = 0.5
    else:
        count = 0
    return count


# In[58]:


overall = indicator(current_spot_rate,current_EMA10) + indicator(current_spot_rate,current_SMA10) + indicator(current_spot_rate,current_EMA50)
overall
