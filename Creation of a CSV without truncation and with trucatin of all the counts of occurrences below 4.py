#!/usr/bin/env python
# coding: utf-8

# This code reads weather data, identifies extreme weather conditions, counts occurrences by day and month, and exports the results to a CSV file. The resultant total number of extreme day-month combinations:253

# In[ ]:


# First let's read and prepare the data import pandas as pd 
# Read the original data df = pd.read_csv('Weather_Parameters_Combined.csv') 
# Define extreme conditions 
df['Date'] = pd.to_datetime(df['Date']) df['Rainfall_Extreme'] = df['Rainfall'] > 20.1 df['Wind_Extreme'] = df['Wind_Speed (m/s)'] > 5.57 df['SWH_Extreme'] = df['SWH'] > 2.1 

# Create day-month column 
df['Day_Month'] = df['Date'].dt.strftime('%d-%m') 

# Count extreme days 
extreme_days = df[df['Rainfall_Extreme'] | df['Wind_Extreme'] | df['SWH_Extreme']] day_month_counts = extreme_days.groupby('Day_Month').size().reset_index(name='Count') 

# Add month and day columns for sorting 
day_month_counts['Month'] = pd.to_datetime('2024-' + day_month_counts['Day_Month'], format='%Y-%d-%m').dt.month day_month_counts['Day'] = pd.to_datetime('2024-' + day_month_counts['Day_Month'], format='%Y-%d-%m').dt.day day_month_counts['Month_Name'] = pd.to_datetime('2024-' + day_month_counts['Day_Month'], format='%Y-%d-%m').dt.strftime('%B') 

# Sort the dataframe export_df = day_month_counts.sort_values(['Month', 'Day']) 
# Select and reorder columns for export 
export_df = export_df[['Day_Month', 'Month_Name', 'Count']] 

# Save to CSV 
csv_filename = 'extreme_weather_calendar.csv' export_df.to_csv(csv_filename, index=False) 

# Display first few rows of the saved file 
print("First few rows of the exported CSV file:") 
print(export_df.head(10)) print("\ File has been saved as:", csv_filename) 
print("Total number of extreme day-month combinations:", len(export_df))


# Creation of another CSV where i've truncated all the counts of occurrences below 4
# 
# Explanation : This code filters a DataFrame for days with 4 or more extreme weather occurrences, sorts the results, saves them to a CSV file, and displays the filtered data.
# 
# The resultant Total number of day-month combinations with 4 or more occurrences:
# 103

# In[ ]:


# Filter for counts >= 4
filtered_df = export_df[export_df['Count'] >= 4].copy()

# Sort by Count in descending order, then by Month and Day
filtered_df = filtered_df.sort_values('Count', ascending=False)

# Save to CSV
filtered_csv_filename = 'extreme_weather_calendar_filtered.csv'
filtered_df.to_csv(filtered_csv_filename, index=False)

# Display results
print("Days with 4 or more extreme weather occurrences:")
print(filtered_df)
print("\
File has been saved as:", filtered_csv_filename)
print("Total number of day-month combinations with 4 or more occurrences:", len(filtered_df))

