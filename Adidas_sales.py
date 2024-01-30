#!/usr/bin/env python
# coding: utf-8

# # Adidas Sales Analysis

# In[21]:


#import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:


#import the dataset
df=pd.read_csv(r'C:\\Users\user\Downloads\Adidas_sales.csv') 
df.head()


# In[3]:


#check for null values
df.isnull().sum()


# In[4]:


#check for duplicates
df.duplicated().sum()


# In[5]:


#changing to proper date time format 
df['Invoice Date'] = pd.to_datetime(df['Invoice Date']) 

#extracting year and month from date
df['Year'] = df['Invoice Date'].dt.year 
df['Month'] = df['Invoice Date'].dt.strftime('%b') 

#calculating total sales 
df['Total_Sales'] = df['Price per Unit'] * df['Units Sold']


# In[6]:


df.head()


# ### top 5 retailers based on sales 

# In[7]:


top_retailers_by_sales = df.groupby('Retailer')['Total_Sales'].sum().nlargest(5) 
formatted_sales = top_retailers_by_sales.map("${:,.2f}".format)
print(formatted_sales)


# ### popular product category 

# In[8]:


popular_product_categories = df['Product Category'].value_counts() 
print(popular_product_categories)


# ### sales trend over year 

# In[9]:


sales_trend_over_Year = df.groupby('Year')['Total_Sales'].sum() 
print(sales_trend_over_Year)


# ### profit based on product category  per region

# In[10]:


profit_per_product_per_region = df.groupby(['Region', 'Product Category'])['Operating Profit'].sum()
print(profit_per_product_per_region)


# ### Which product category has the highest total sales and operating profit?

# In[18]:


# Group the data by 'Product' and calculate total sales and operating profit
product_summary = df.groupby('Product Category')[['Total_Sales', 'Operating Profit']].sum()

# Find the product category with the highest total sales and operating profit
max_sales_product = product_summary['Total_Sales'].idxmax()
max_profit_product = product_summary['Operating Profit'].idxmax()

print("Product category with the highest total sales:", max_sales_product)
print("Product category with the highest operating profit:", max_profit_product)


# ### Total Sales per Product Category

# In[11]:


color=['#FF5733', '#5A9BD4', '#FFD700']

# Create the barplot
sns.barplot(x='Product Category', y='Total_Sales', data=df, palette=color)

# Add a title
plt.title('Total Sales per Product Category', fontsize=16, fontweight='bold')

# Label the axes and customize their fonts
plt.xlabel('Product Category', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)

# Customize y-axis labels with commas and specify their font size
from matplotlib.ticker import FuncFormatter
def format_func(value, tick_number):
    return f"${value:,.0f}"
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))
plt.yticks(fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=12)

# Customize the plot background color
plt.gca().set_facecolor('#F5F5F5')

# Customize the grid lines
sns.despine(left=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)


# Add data labels on top of the bars
for p in plt.gca().patches:
    plt.gca().annotate(f"${p.get_height():,.0f}", 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', fontsize=12, 
                       color='black', xytext=(0, 5),
                        textcoords='offset points')

plt.show()


# ### sales proportion by sales method

# In[14]:


# Define a custom color palette with beautiful colors
custom_colors = ['#FF6B6B', '#FFD166', '#06D6A0']

# Create a figure and set its size
plt.figure(figsize=(8, 8))

# Create the pie chart with custom colors and labels
sales_method_counts = df['Sales Method'].value_counts()
plt.pie(sales_method_counts, labels=sales_method_counts.index, 
        autopct='%1.1f%%', colors=custom_colors, startangle=90)

# Add a title
plt.title('Sales Proportion by Sales Method', fontsize=16, fontweight='bold')

# Add a legend with custom colors
plt.legend(sales_method_counts.index, loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Add a shadow effect to the pie chart
plt.gca().set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.gca().add_artist(plt.Circle((0, 0), 0.7, fc='white'))

# Show the plot
plt.tight_layout()
plt.show()


# ### Total sales by retailer and product category

# In[15]:


# Define a custom color palette with beautiful colors
custom_palette = ['#FF6B6B', '#FFD166', '#06D6A0']

# Create a figure and set its size
plt.figure(figsize=(12, 8))

# Create the grouped bar chart with custom colors and labels
sns.barplot(x='Retailer', y='Total_Sales', hue='Product Category', data=df, palette=custom_palette)

# Add a title
plt.title('Total Sales by Retailer and Product Category', fontsize=16, fontweight='bold')

# Customize x-axis labels rotation for better readability
plt.xticks(rotation=45, fontsize=12)

# Customize y-axis labels with commas and specify their font size
from matplotlib.ticker import FuncFormatter
def format_func(value, tick_number):
    return f"${value:,.0f}"
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))
plt.yticks(fontsize=12)

# Customize the legend
plt.legend(title='Product Category', title_fontsize=12, fontsize=10)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize the background color of the plot
plt.gca().set_facecolor('#F5F5F5')

# Show the plot
plt.tight_layout()
plt.show()


# ### What is the overall trend of total sales and operating profit over the years?

# In[16]:


# Group by year and calculate total sales and operating profit
yearly_summary = df.groupby('Year')[['Total_Sales', 'Operating Profit']].sum().reset_index()

# Set Seaborn style
sns.set(style="whitegrid")

# Create a figure and set its size
plt.figure(figsize=(12, 6))

# Plotting the trend using Seaborn
sns.lineplot(data=yearly_summary, x='Year', y='Total_Sales', marker='o', label='Total Sales')
sns.lineplot(data=yearly_summary, x='Year', y='Operating Profit', marker='o', label='Operating Profit')

# Customize the plot title and labels
plt.title('Overall Trend of Total Sales and Operating Profit Over Years', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount (in dollars)', fontsize=12)

# Customize y-axis labels with commas and specify their font size
def format_func(value, tick_number):
    return f"${value:,.0f}"
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))
plt.yticks(fontsize=10)

# Add a legend with adjusted font size
plt.legend(fontsize=12)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize the background color of the plot
plt.gca().set_facecolor('#F5F5F5')

# Show the plot
plt.tight_layout()
plt.show()


# ### How do in-store and outlet sales compare in terms of total sales and operating profit?

# In[17]:


# Group the data by 'Sales Method' and calculate total sales and operating profit
sales_comparison = df.groupby('Sales Method')[['Total_Sales', 'Operating Profit']].sum()

# Create a figure and set its size
plt.figure(figsize=(12, 8))

# Define custom colors for the bars
colors = ['#FF6B6B', '#06D6A0']

# Create the bar chart with stacked bars and custom colors
ax = sales_comparison.plot(kind='bar', stacked=True, color=colors)

# Customize the plot title and labels
plt.title('Comparison of In-Store and Outlet Sales', fontsize=16, fontweight='bold')
plt.xlabel('Sales Method', fontsize=12)
plt.ylabel('Amount (in dollars)', fontsize=12)

# Customize x-axis labels rotation for better readability
plt.xticks(rotation=0, fontsize=10)

# Customize y-axis labels with commas and specify their font size
from matplotlib.ticker import FuncFormatter
def format_func(value, tick_number):
    return f"${value:,.0f}"
ax.yaxis.set_major_formatter(FuncFormatter(format_func))
plt.yticks(fontsize=10)

# Add data labels on top of the bars
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, 
                color='black', xytext=(0, 5),
                textcoords='offset points')

# Customize the legend with adjusted font size and title
plt.legend(title='Metrics', fontsize=12)

# Customize the background color of the plot
ax.set_facecolor('#F5F5F5')

# Show the plot
plt.tight_layout()
plt.show()


# ### How do sales vary across different states and cities?

# In[19]:


# Create a figure and set its size
plt.figure(figsize=(10, 5))

# Group the data by 'Region' and calculate total sales for each region
region_sales = df.groupby('Region')['Total_Sales'].sum()

# Define a custom color palette with visually appealing colors
custom_palette = ['#FF6B6B', '#FFD166', '#06D6A0', '#118AB2', '#073B4C']

# Create the bar chart with custom colors
ax = region_sales.plot(kind='bar', color=custom_palette)

# Customize the plot title and labels
plt.title('Sales Variation Across Different Regions', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales (in dollars)', fontsize=12)

# Customize x-axis labels rotation for better readability
plt.xticks(rotation=0, fontsize=10)

# Customize y-axis labels with commas and specify their font size
from matplotlib.ticker import FuncFormatter
def format_func(value, tick_number):
    return f"${value:,.0f}"
ax.yaxis.set_major_formatter(FuncFormatter(format_func))
plt.yticks(fontsize=10)

# Add data labels on top of the bars
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

# Customize the background color of the plot
ax.set_facecolor('#F5F5F5')

# Show the plot
plt.tight_layout()
plt.show()


# ### Total sales for each combination of product category and gender type

# In[20]:


plt.figure(figsize=(10, 8))

heatmap_data = df.pivot_table(index='Product Category', columns='Gender Type', values='Total_Sales')
# Use a different color palette (Blues in this case)
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt=".0f", linewidths=0.5)

# Add axis labels
plt.xlabel('Gender Type', fontsize=12)
plt.ylabel('Product Category', fontsize=12)

# Increase font size of annotations
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Modify title
plt.title('Normalized Heatmap of Total Sales by Product Category and Gender Type', fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


# ### Statistical Analysis

# In[22]:


summary_statistics = df.describe()
print(summary_statistics)


# ### T-statistics and P value

# In[29]:


men_sales = df[df['Gender Type'] == 'Men']['Total_Sales']
women_sales = df[df['Gender Type'] == 'Women']['Total_Sales']
t_statistic, p_value = stats.ttest_ind(men_sales, women_sales)
print("T-statistic:", round(t_statistic, 2))
print("P-value:", p_value)


# ### F-statistics and ANOVA

# In[27]:


regions = df['Region'].unique()
grouped_data = [df[df['Region'] == region]['Total_Sales'] for region in regions]

f_statistic, p_value_anova = stats.f_oneway(*grouped_data)
print("F-statistic:", round(f_statistic, 2))
print("P-value (ANOVA):", p_value_anova)


# ## Executive summary

# ### Sales and Operating Profit Trends:
# The overall sales trend for Adidas products is showing a consistent increase over time.
# However, a notable finding is that the operating profit has increased at a greater rate.
# This indicates an improvement in profitability and operational efficiency.

# ### Regional Analysis
# The West region stands out with the highest sales figures.
# This suggests a strong market demand for Adidas products in the West region.
# 
# For regions with lower sales like Midwest,there is an opportunity for strategic interventions to boost sales.This could involve targeted marketing campaigns, promotions, or assessing the product mix to better align with local preferences.

# ### Product Category Insights
# Footwear emerges as the leading product category, contributing significantly to total sales. 
# The specific product categories, such as "Street Footwear" and "Athletic Footwear," demonstrate strong sales performance

# ### Statistical analysis
# T-test indicates a significant difference in a variable (e.g., sales or profit) between Men and Women in the dataset.
# 
# ANOVA reveals significant differences in a numerical variable (e.g., sales or profit) among various 'Product Category' groups.
# 
# Gender and 'Product Category' have a notable impact on key performance indicators (KPIs) such as sales and profitability in the Adidas sales dataset

# In[ ]:




