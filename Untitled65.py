#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# In[2]:


df=pd.read_csv(r'C:\\Users\user\Downloads\Adidas.csv')
print(df)


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.columns


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


df.duplicated().sum()


# In[10]:


df.isnull().sum()


# In[11]:


df.nunique()


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[14]:


df['Retailer'].unique()


# In[15]:


df['Retailer'].value_counts()


# In[21]:


plt.figure(figsize=(8,5))
sns.countplot(df['Retailer'], data = df, palette = 'husl').set(title="Count per Retailers")
plt.xticks(rotation = 90)
plt.show()


# In[18]:


df['Region'].value_counts()


# In[22]:


plt.figure(figsize=(8,5))
sns.countplot(df['Region'], data = df, palette = 'flare').set(title="Count of Region")
plt.xticks(rotation = 90)
plt.show()


# In[24]:


plt.figure(figsize=(10,5))
sns.countplot(df['Region'], data = df, hue = "Retailer", palette = 'husl').set(title="Count of Retailers based on Region")
plt.xticks(rotation = 90)
plt.show()


# In[25]:


df['Sales Method'].value_counts()


# In[33]:


data = [4889, 3019, 1740]
keys = ['Online', 'Outlet', 'In-Store']
cols = ['c', 'pink', 'grey']
plt.pie(data, labels=keys,colors = cols, startangle = 90, shadow = True, autopct='%.0f%%', radius = 1.2)
plt.title("Count of Sales Method")
plt.legend(loc='upper left')
plt.show()


# In[35]:


df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])


# In[36]:


df['Year'] = df['Invoice Date'].dt.year
df


# In[37]:


df['Year'].value_counts()


# In[38]:


plt.figure(figsize=(5,5))
sns.countplot(df['Year'], data = df, palette = 'hls').set(title="Sales per year")
plt.xticks(rotation = 90)
plt.show()


# In[42]:


df['Price per Unit'] = df['Price per Unit'].astype(float)
plt.figure(figsize=(10,6))
sns.barplot(x = df['Product'], y = df['Price per Unit'], data = df, palette = 'flare').set(title="Product price")
plt.xticks(rotation = 90)
plt.show()


# In[49]:


Total_sales= df[['Product','Total Sales(in dollars)']].groupby('Product').sum()
Total_sales


# In[54]:


Total_sales.plot(kind='bar',figsize=(12,7),title='Total sales (in dollar) per Product', color='c')
plt.show()


# In[53]:


Total_profit= df[['Product','Operating Profit(in dollars)']].groupby('Product').sum()
Total_profit


# In[59]:


Total_profit.plot(kind='bar',figsize=(12,7),title='Total profit (in dollar) per Product', color='pink')
plt.show()


# In[ ]:




