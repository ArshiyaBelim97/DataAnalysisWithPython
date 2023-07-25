#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.read_excel(r'/Users/arshiyabelim/Desktop/DataAnalysis Projects/archive/Career Mode player datasets - FIFA 15-21.xlsx')
print(df.head())


# In[14]:


# converting height from int to float
df['height_cm'] = df['height_cm'].astype(float)
print(df['height_cm'].dtypes)


# In[15]:


#converting weight from int to float
df['weight_kg'] = df['weight_kg'].astype(float)
print(df['weight_kg'].dtypes)


# In[16]:


#Checking converted data types
df.weight_kg.dtypes
df.height_cm.dtypes


# In[17]:


# Seperate the Joined column with year, month and day
# df['year'] = df['joined'].dt.year
df[["year", "month", "day"]] = df["joined"].strftimes.split("-", expand = True)
print(df)


# In[18]:


df.joined.dtypes


# In[21]:


#deleting the "defending_marking" column which had no data
df.drop(['defending_marking'],axis=1)


# In[9]:


#defining some columns as useless and delete them so that the useless data would not be there in the final data 
useless_column = ['dob','sofifa_id','player_url','long_name','body_type','real_face','nation_position','loaned_from','nation_jersey_number']
df.drop(useless_column, axis = 1)


# In[11]:


#counting player's BMI from their height and weight
df['BMI'] = df ['weight_kg'] / (df['height_cm'] / 100) ** 2


# In[12]:


df.head()


# In[14]:


#removing null values from the data 
columns = ['ls','st','rs','lw','lf','cf','rf','rw','lam','cam','ram','lm','lcm','cm','rcm','rm','lwb','ldm', 'cdm','rdm','rwb','lb','lcb','cb','rcb','rb']
for col in columns:
  df[col] = df[col].str.split('+',n=1,expand = True)[0]


# In[15]:


df[columns] = df[columns].fillna(0)
df[columns] = df[columns].astype(int)


# In[16]:


columns = ['dribbling','defending','physic','passing','shooting','pace']
df[columns].isnull().sum()


# In[17]:


for col in columns:
  df[col] = df[col].fillna(df[col].median())


# In[18]:


df = df.fillna(0)
df.isnull().sum() #Verifying it Should be all zero


# In[ ]:




