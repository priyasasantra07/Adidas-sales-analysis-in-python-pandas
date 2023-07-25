#!/usr/bin/env python
# coding: utf-8

# # Adidas Sales Analysis

# In[5]:


import pandas as pd


# In[2]:


df=pd.read_csv(r'C:\\Users\user\Downloads\Adidas_sales.csv')
print(df)


# In[3]:


df.head()


# In[63]:


df.tail()


# In[69]:


#changing to proper date time format
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])


# In[71]:


#extracting year and month from date
df['Year'] = df['Invoice Date'].dt.year
df['Month'] = df['Invoice Date'].dt.month


# In[73]:


#calculating profit per unit
df['Profit_per_Unit'] = df['Operating Profit'] / df['Units Sold']


# In[74]:


#calculating total sales
df['Total_Sales'] = df['Price per Unit'] * df['Units Sold']


# In[9]:


df.head()


# In[64]:


df.shape


# In[65]:


df.columns


# In[66]:


df.duplicated().sum()


# In[67]:


df.isnull().sum()


# In[68]:


df.info()


# In[76]:


#top 5 retailers based on sales
top_retailers_by_sales = df.groupby('Retailer')['Total_Sales'].sum().nlargest(5)
print(top_retailers_by_sales)


# In[77]:


#popular product category
popular_product_categories = df['Product Category'].value_counts()
print(popular_product_categories)


# In[78]:


#sales trend over time
sales_trend_over_time = df.groupby('Invoice Date')['Total_Sales'].sum()
print(sales_trend_over_time)


# In[79]:


#sales trend over year
sales_trend_over_Year = df.groupby('Year')['Total_Sales'].sum()
print(sales_trend_over_Year)


# In[80]:


#profit based on product category
profit_per_category = df.groupby('Product Category')['Profit_per_Unit'].mean()
print(profit_per_category)


# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt


# # Visualization

# # Total Sales per Product Category

# In[32]:


color=['pink','silver','c']
sns.barplot(x='Product Category', y='Total_Sales', data=df, palette=color)
plt.title('Total Sales per Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# # Sales Trend Over Time

# In[26]:


plt.figure(figsize=(10, 5))
sns.lineplot(x='Invoice Date', y='Total_Sales', data=df)
plt.title('Sales Trend Over Time')
plt.xlabel('Invoice Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# # Sales Trend Over Year

# In[35]:


plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Total_Sales', data=df)
plt.title('Sales Trend Over Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# # Relationship between Total Sales and Profit per Unit

# In[36]:


plt.figure(figsize=(8, 5))
sns.scatterplot(x='Total_Sales', y='Profit_per_Unit', data=df)
plt.title('Relationship between Total Sales and Profit per Unit')
plt.xlabel('Total Sales')
plt.ylabel('Profit per Unit')
plt.show()


# # Sales Proportion by Sales Method

# In[42]:


plt.figure(figsize=(6, 6))
color=['pink','silver','c']
df['Sales Method'].value_counts().plot(kind='pie', autopct='%1.1f%%',radius = 1,colors=color)
plt.title('Sales Proportion by Sales Method')
plt.ylabel('')
plt.legend(loc='upper left')
plt.show()


# # Correlation Matrix

# In[43]:


correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# # Distribution of Operating Margin by Product Category

# In[45]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='Product Category', y='Operating Margin', data=df)
plt.title('Distribution of Operating Margin by Product Category')
plt.xticks(rotation=45)
plt.show()


# # Total Sales by Retailer and Product Category

# In[49]:


plt.figure(figsize=(10, 6))
color = {'Apparel': 'pink', 'Street Footwear': 'silver', 'Athletic Footwear': 'c'}
sns.barplot(x='Retailer', y='Total_Sales', hue='Product Category', data=df, palette=color)
plt.title('Total Sales by Retailer and Product Category')
plt.xticks(rotation=45)
plt.show()


# # Kernel Density Estimation

# In[53]:


plt.figure(figsize=(8, 6))
sns.kdeplot(data=df['Total_Sales'], fill=True)
plt.title('Kernel Density Estimation of Total Sales')
plt.show()


# In[54]:


import pandas as pd
from scipy import stats


# In[55]:


summary_statistics = df.describe()
print(summary_statistics)


# # T-statistics and P value

# In[57]:


men_sales = df[df['Gender Type'] == 'Men']['Total_Sales']
women_sales = df[df['Gender Type'] == 'Women']['Total_Sales']
t_statistic, p_value = stats.ttest_ind(men_sales, women_sales)
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# # F statistics and ANOVA

# In[59]:


regions = df['Region'].unique()
grouped_data = [df[df['Region'] == region]['Total_Sales'] for region in regions]

f_statistic, p_value_anova = stats.f_oneway(*grouped_data)
print("F-statistic:", f_statistic)
print("P-value (ANOVA):", p_value_anova)


# # Overall, based on the statistical results obtained from the T-test and ANOVA, we can conclude that :
# 1. T-test indicates a significant difference in a variable (e.g., sales or profit) between Men and Women in the dataset.
# 
# 2. ANOVA reveals significant differences in a numerical variable (e.g., sales or profit) among various 'Product Category' groups.
# 
# 3. Gender and 'Product Category' have a notable impact on key performance indicators (KPIs) such as sales and profitability in the Adidas sales dataset
# 
# 

# In[ ]:




