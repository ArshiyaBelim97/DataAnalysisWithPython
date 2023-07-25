#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv(r'/Users/arshiyabelim/Desktop/DataAnalysis Projects/jobPosting/Uncleaned_DS_jobs.csv')


# In[8]:


df.drop('index',inplace=True, axis=1)
df.head()


# In[9]:


df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0].replace('$','').replace('K',''))


# In[11]:


df['Salary Estimate'].unique()


# In[12]:


df['Salary Estimate'][0].split('-')


# In[13]:


df['Minimum Salary']=df['Salary Estimate'].apply(lambda x: x.split('-')[0]).astype(int)
df['Maximum Salary']=df['Salary Estimate'].apply(lambda x: x.split('-')[1]).astype(int)
df['Average Salary']=round((df['Minimum Salary']+df['Maximum Salary'])/2,2)


# In[14]:


df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['SQL']=df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['Machine Learning']=df['Job Description'].apply(lambda x: 1 if 'machine learning' or 'ml' in x.lower() else 0)
df['Hadoop']=df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df['Big Data']=df['Job Description'].apply(lambda x: 1 if 'big data' in x.lower() else 0)
df['Excel']=df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0)
df['Tableau']=df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['AWS']=df['Job Description'].apply(lambda x: 1 if 'amazon web services' or 'aws' in x.lower() else 0)
df['Spark']=df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)


# In[15]:


ll=['Python','SQL','Machine Learning','Hadoop','Big Data','Excel','Tableau','AWS','Spark']
for i in ll:
    print(df[i].value_counts())


# In[16]:


df['Company Name'] = df['Company Name'].apply(lambda x: x.split('\n')[0])


# In[18]:


df.columns


# In[19]:


df.dtypes


# In[20]:


df[df['Competitors']=='-1'].shape


# In[21]:


del df['Competitors']
df['Rating'].unique()


# In[22]:


df['Rating'].replace((-1),0,inplace=True)
df[df['Rating']==-1].shape


# In[23]:


df.sort_values(by='Rating', ascending=True)


# In[ ]:




