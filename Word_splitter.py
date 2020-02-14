#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv' 


# In[46]:


df=pd.read_csv(url) #using pandas to read the contents of the url


# In[47]:


def word_spliter(df):
    df['temp column']=df['Tweets'].str.lower() #temporal column that contains the tweets in lowercase
    df['Split tweets']=df['temp column'].str.rsplit() #slitting the words of temporal column into a new column 'Split tweets'
    df = df.drop('temp column', 1)  #delete temporal column.

    return df


# In[44]:


word_spliter(df)


# In[ ]:




