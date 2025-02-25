#!/usr/bin/env python
# coding: utf-8

# The code snippet processes weather data to assess the impact of extreme weather on fishing days, calculates economic losses, and provides insights and recommendations based on the analysis

# In[ ]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns from datetime 
import datetime import calendar 

# Read the weather data 
df = pd.read_csv('Weather_Parameters_Combined.csv') 
df['Date'] = pd.to_datetime(df['Date']) 
df['Month'] = df['Date'].dt.month 
df['Day'] = df['Date'].dt.day 
df['Year'] = df['Date'].dt.year 

# Define thresholds for extreme weather 
RAINFALL_THRESHOLD = 50 # mm 
WIND_SPEED_THRESHOLD = 5 # m/s 
SWH_THRESHOLD = 2 

# meters # Create binary indicators for extreme weather 
df['Extreme_Rainfall'] = df['Rainfall'] > RAINFALL_THRESHOLD 
df['Extreme_Wind'] = df['Wind_Speed (m/s)'] > WIND_SPEED_THRESHOLD 
df['Extreme_SWH'] = df['SWH'] > SWH_THRESHOLD


# Calculate days with any extreme weather 
df['Extreme_Weather_Day'] = (df['Extreme_Rainfall'] | df['Extreme_Wind'] | df['Extreme_SWH']).astype(int) 

# Monthly analysis 
monthly_stats = df.groupby(['Year', 'Month']).agg({ 'Extreme_Weather_Day': 'sum', 'Extreme_Rainfall': 'sum', 'Extreme_Wind': 'sum', 'Extreme_SWH': 'sum' }).reset_index() 

# Calculate potential fishing days and economic impact 
DAILY_INCOME = 11000 / 30 

# Average monthly income divided by 30 days 
monthly_stats['Days_in_Month'] = monthly_stats.apply( lambda x: calendar.monthrange(int(x['Year']), int(x['Month']))[1], axis=1) 
monthly_stats['Potential_Fishing_Days'] = monthly_stats['Days_in_Month'] - monthly_stats['Extreme_Weather_Day'] 
monthly_stats['Economic_Loss'] = monthly_stats['Extreme_Weather_Day'] * DAILY_INCOME 

# Calculate year-over-year trends 
yearly_trends = monthly_stats.groupby('Year').agg({ 'Extreme_Weather_Day': 'sum', 'Potential_Fishing_Days': 'sum', 'Economic_Loss': 'sum' }).reset_index() 

# Plotting yearly trends 
plt.figure(figsize=(15, 7)) 
plt.plot(yearly_trends['Year'], yearly_trends['Extreme_Weather_Day'], marker='o', linewidth=2, markersize=8) 
plt.title('Yearly Trend of Extreme Weather Days') 
plt.xlabel('Year') 
plt.ylabel('Number of Extreme Weather Days') 
plt.grid(True) 
plt.tight_layout() plt.show() 

# Calculate and plot monthly patterns 
monthly_patterns = monthly_stats.groupby('Month').agg({ 'Extreme_Weather_Day': 'mean', 'Economic_Loss': 'mean' }).reset_index()
plt.figure(figsize=(15, 7)) 
sns.barplot(data=monthly_patterns, x='Month', y='Extreme_Weather_Day', color='red', alpha=0.6) 
plt.title('Average Monthly Distribution of Extreme Weather Days') 
plt.xlabel('Month') plt.ylabel('Average Number of Extreme Weather Days') 
plt.grid(True, axis='y') 
plt.tight_layout() 
plt.show() 

# Calculate key metrics and insights 
total_days_lost = yearly_trends['Extreme_Weather_Day'].mean() 
total_economic_impact = yearly_trends['Economic_Loss'].mean() 
worst_month = monthly_patterns.loc[monthly_patterns['Extreme_Weather_Day'].idxmax()] 
trend_coefficient = np.polyfit(range(len(yearly_trends)), yearly_trends['Extreme_Weather_Day'], 1)[0] 

# Print insights 
print("\ Advanced Prescriptive Analysis Insights:") 
print("\ 1. Impact Assessment:") 
print(f"- Average Annual Days Lost: {total_days_lost:.1f}") 
print(f"- Average Annual Economic Impact: ₹{total_economic_impact:,.2f}") 
print(f"- Most Challenging Month: {calendar.month_name[int(worst_month['Month'])]} " f"({worst_month['Extreme_Weather_Day']:.1f} days)") 
print("\ 2. Trend Analysis:") 
print(f"- Year-over-Year Trend: {trend_coefficient:.2f} days/year") 
print("- Long-term Projection: " + ("Increasing" if trend_coefficient > 0 else "Decreasing") + " frequency of extreme weather events") 

# Calculate risk levels and recommendations 
monthly_patterns['Risk_Level'] = pd.qcut(monthly_patterns['Extreme_Weather_Day'], q=3, labels=['Low', 'Medium', 'High']) 
print("\ 3. Risk Assessment and Recommendations:") for _, row in monthly_patterns.sort_values('Extreme_Weather_Day', ascending=False).head(3).iterrows(): month_name = calendar.month_name[int(row['Month'])] 
    print(f"\ {month_name} (High Risk):") 
    print(f"- Average Lost Days: {row['Extreme_Weather_Day']:.1f}") 
    print(f"- Economic Impact: ₹{row['Economic_Loss']:,.2f}") 
    print("Recommendations:") 
    print("- Consider alternative income sources") 
    print("- Plan maintenance and repairs") 
    print("- Focus on savings during better months") 
    
    # Calculate adaptation metrics 
    adaptation_potential = (yearly_trends['Extreme_Weather_Day'].max() - yearly_trends['Extreme_Weather_Day'].min()) / \ yearly_trends['Extreme_Weather_Day'].mean() * 100 
    print("\ 4. Adaptation Strategies:") 
    print(f"- Adaptation Potential: {adaptation_potential:.1f}%") 
    print("- Short-term Recommendations:") 
    print(" * Implement early warning systems") 
    print(" * Invest in weather-resistant equipment") 
    print("- Long-term Recommendations:") 
    print(" * Develop alternative livelihood programs") 
    print(" * Create community-based insurance schemes") 
    print(" * Establish emergency funds")


# The code snippet performed statistical analysis on extreme weather event data, calculating z-scores, mean, standard deviation, and impact severity at various thresholds, followed by visualizing the results

# In[ ]:


# Analyze the cumulative impact of extreme weather events with different thresholds thresholds = [1, 2, 3, 4, 5] 
# Different thresholds for extreme weather event counts impact_analysis = [] for threshold in thresholds: 
# Filter data for events above the threshold

filtered_data = df[df['Extreme_Weather_Day'] >= threshold] 
# Calculate total lost days and economic impact 
total_lost_days = filtered_data['Extreme_Weather_Day'].sum() 
total_economic_loss = total_lost_days * DAILY_INCOME 

# Append results 
impact_analysis.append({ 'Threshold': threshold, 'Total_Lost_Days': total_lost_days, 'Total_Economic_Loss': total_economic_loss }) 

# Convert to DataFrame for better visualization 
impact_df = pd.DataFrame(impact_analysis) 

# Plot the results 
plt.figure(figsize=(12, 6)) 
plt.plot(impact_df['Threshold'], impact_df['Total_Lost_Days'], marker='o', label='Total Lost Days') 
plt.plot(impact_df['Threshold'], impact_df['Total_Economic_Loss'], marker='s', label='Total Economic Loss (INR)') 
plt.title('Impact of Different Thresholds for Extreme Weather Events') 
plt.xlabel('Threshold (Number of Extreme Weather Events)') plt.ylabel('Impact') 
plt.legend() 
plt.grid(True) 
plt.tight_layout() 
plt.show() 

# Display the impact analysis table print(impact_df)

