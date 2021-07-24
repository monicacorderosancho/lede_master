#!/usr/bin/env python
# coding: utf-8

# In[1]:


### This is link to database https://webapps.jcope.ny.gov/public/ |||| sort by Pharmaceuticals/ Health Products  
import pandas as pd


# ## Here is the data

# In[2]:


df = pd.read_excel("JCOPE_2019.xlsx")


# In[3]:


df2 = pd.read_excel("JCOPE_2020.xlsx")


# In[4]:


df3 = pd.read_excel("JCOPE_2021.xlsx")


# ## Checking rows and columns 

# In[5]:


df.shape


# In[6]:


df2.shape


# In[7]:


df3.shape


# ## Cheking data types

# In[8]:


## note: TOTAL COMPENSATION and TOTAL EXPENSES are integer
df.dtypes


# ## Checking what's here

# In[9]:


df.head(3)


# ## Concat DataFrame

# In[10]:


### axis=0 = vertical /  horizontal = 1 df4 = pd.concat([df,df1,df2],axis=0)

df4 = pd.concat([df,df2,df3],axis=0)


# In[11]:


df4.shape


# ## Renamed columns

# In[12]:


df4 = df4.rename(columns = {'SUBJECT LOBBIED':'subject_lobbied','YEAR':'year'})


# In[13]:



df4 = df4.rename(columns = {'FILING TYPE':'filing_type','FILING PERIOD':'filing_period','SUBJECT LOBBIED':'subject_lobbied'})


# In[14]:


df4 = df4.rename(columns = {'CONTRACTUAL CLIENT':'contractual_client','BENEFICIAL CLIENT':'beneficial_client'})


# In[15]:


df4 = df4.rename(columns = { 'TOTAL EXPENSES': 'total_expenses', 'TOTAL COMPENSATION': 'total_compensation'})


# In[16]:


df4 = df4.rename(columns = {'PRINCIPAL LOBBYIST':'principal_lobbyist'})


# In[17]:


df4.head(20)


# In[18]:


### regular expresion 
get_ipython().system('pip install regex ')


# In[19]:


df4.shape


# In[20]:


### principal_lobbyist case=False == give everything indepen how is written a=False ignore missing values
### I need to separate the company name and its address. 
### These are the patterns I found: INC | LLC | some addresses start with a number.

df4[df4.principal_lobbyist.str.contains('INC.',case=False,na=False)].principal_lobbyist.value_counts()


# In[21]:


### ~ exclude the rows that contain INC 

df4[~(df4.principal_lobbyist.str.contains('INC.',case=False,na=False))].principal_lobbyist.value_counts()


# In[22]:


pd.set_option("display.max_rows", None)


# In[23]:


df4['lobbyst_name'] = df4.principal_lobbyist.str.extract(r'(.*)\d+')


# In[24]:


df4.lobbyst_name.value_counts(dropna=False)


# ## Main LOBBYIST by year

# In[25]:


df4.groupby('year').principal_lobbyist.value_counts(dropna=False,ascending=True)


# ## Main CONTRACTUAL CLIENT 

# In[26]:


df4.groupby('year').contractual_client.value_counts(dropna=False,ascending=True)


# ## TOTAL COMPENSATION analysis 

# # Delete dolar sign and comma 

# In[27]:


# Permanently change Age to be an integer df.Age = df.Age.astype(int) Como se le $ y lo hago permanente 
df4.total_compensation = df4.total_compensation.str.replace('$', '')


# In[28]:


## Replace delete ,    
df4.total_compensation = df4.total_compensation.str.replace(',', '')
df4.head(4)


# In[29]:


### convert to int
### column_name = column_name.somefunction()
df4.total_compensation = df4.total_compensation.fillna(0).astype('int')
df4.head (4)


# In[44]:


df4.groupby(‘year’).plot(x='total_expenses', y='subject_lobbied')


# ## TOTAL EXPENSES vs PRINCIPAL LOBBYIST

# ## Delete dollar sign and comma
# 

# In[45]:


### Delete $ sign df4.total_compensation = df4.total_compensation.str.replace('$', '')
df4.total_expenses = df4.total_expenses.str.replace('$', '')
df4.head(4)


# In[46]:


### Delete , 
df4.total_expenses = df4.total_expenses.str.replace(',', '')
df4.head(4)


# In[ ]:




