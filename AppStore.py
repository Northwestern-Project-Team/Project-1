#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import numpy as np


# In[2]:


# Name of the CSV file
csv_path = 'googleplaystore.csv'


# In[3]:


# The read the CSV file in pandas
googlestore = pd.read_csv(csv_path)
googlestore.head()


# In[4]:


# Delete column "Current Ver" , "Android Ver" and "Genres"
del googlestore["Current Ver"]
del googlestore["Android Ver"] 
del googlestore["Genres"] 
googlestore.head()


# In[5]:


# Identify incomplete rows
googlestore.count()


# In[6]:


# Drop all rows with missing information
googlestore = googlestore.dropna(how='any')


# In[7]:


# Verify dropped rows
googlestore.count()


# In[8]:


# The "Reviews" and "Price" column are the wrong data types. They should be numeric.
googlestore.dtypes


# In[9]:


# Convert the datatype of 'Reviews' column
googlestore['Reviews'] = pd.to_numeric(googlestore['Reviews'])
# Remove dollar sign and convert the datatype of 'Price' column
googlestore['Price'] = googlestore['Price'].str.replace('$', '')
googlestore['Price'] = pd.to_numeric(googlestore['Price'])


# In[10]:


# Verify datatypes have been changed
googlestore.dtypes


# In[11]:


# Push the cleaned dataset to a new CSV file
googlestore.to_csv("googlestore_clean.csv",
                  encoding="utf-8", index=False, header=True)


# In[12]:


# Display an overview of the Category column
googlestore['Category'].value_counts()


# In[13]:


googlestore['Rating'].value_counts()


# In[14]:


googlestore['Size'].value_counts()


# In[15]:


googlestore['Installs'].value_counts()


# In[16]:


googlestore['Type'].value_counts()


# In[17]:


googlestore['Price'].value_counts()


# In[18]:


googlestore['Content Rating'].value_counts()


# In[19]:


googlestore['Last Updated'].value_counts()


# In[20]:


# Display a statistical overview
googlestore.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




