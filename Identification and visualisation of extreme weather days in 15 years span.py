#!/usr/bin/env python
# coding: utf-8

# This code snippet imports the pandas library, loads a CSV file containing weather parameters into a DataFrame, and prints the first few rows along with the data structure information.

# In[ ]:


# Importing necessary libraries
import pandas as pd

# Load the dataset
file_path = 'Weather_Parameters_Combined.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the data
print(data.head())
print(data.info())


# The code identifies extreme weather days based on specified thresholds and counts their occurrences by day and month. 

# In[ ]:


# Convert the 'Date' column to datetime format for easier manipulation
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Extract Day-Month for grouping purposes
data['Day_Month'] = data['Date'].dt.strftime('%d-%m')

# Identify extreme days based on the given thresholds
data['Extreme'] = (data['Rainfall'] > 20.1) | (data['Wind_Speed (m/s)'] > 5.57) | (data['SWH'] > 2.1)

# Filter only extreme days
extreme_days = data[data['Extreme']]

# Group by Day-Month and count occurrences
day_month_counts = extreme_days.groupby('Day_Month').size().reset_index(name='Count')

# Sort by Day-Month for better readability
day_month_counts = day_month_counts.sort_values(by='Day_Month')

# Display the result
print(day_month_counts.head())  


# This code snippet generates a calendar heatmap visualization of extreme weather days over a 15-year span, calculates summary statistics, and identifies the top 10 most extreme day-month combinations.

# In[ ]:


# Create a more detailed analysis including which parameters exceeded thresholds
data['Rainfall_Extreme'] = data['Rainfall'] > 20.1
data['Wind_Extreme'] = data['Wind_Speed (m/s)'] > 5.57
data['SWH_Extreme'] = data['SWH'] > 2.1

# Create a calendar heatmap-style visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Convert Day-Month to a more readable format for plotting
day_month_counts['Month'] = pd.to_datetime(day_month_counts['Day_Month'], format='%d-%m').dt.month
day_month_counts['Day'] = pd.to_datetime(day_month_counts['Day_Month'], format='%d-%m').dt.day

# Create a pivot table for the heatmap
heatmap_data = day_month_counts.pivot(index='Day', columns='Month', values='Count')

# Plot the heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt='.0f', cbar_kws={'label': 'Number of Extreme Days'})
plt.title('Calendar Heatmap of Extreme Weather Days (15-year span)')
plt.xlabel('Month')
plt.ylabel('Day')
plt.show()

# Calculate some summary statistics
print("\
Summary Statistics:")
print("Total number of extreme days:", len(extreme_days))
print("Maximum occurrences in a single day-month:", day_month_counts['Count'].max())
print("Average occurrences per day-month:", round(day_month_counts['Count'].mean(), 2))

# Show the top 10 most extreme day-month combinations
print("\
Top 10 most extreme day-month combinations:")
print(day_month_counts.nlargest(10, 'Count'))


# In[ ]:




