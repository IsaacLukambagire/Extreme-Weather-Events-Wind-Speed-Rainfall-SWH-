#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Load and analyze the original dataset
df = pd.read_csv('Weather_Parameters_Combined.csv')

# Apply thresholds to identify extreme weather events
extreme_events = df[
    (df['Rainfall'] >= 20.1) |
    (df['Wind_Speed (m/s)'] >= 5.57) |
    (df['SWH'] >= 2.1)
]

# Monthly analysis
extreme_events['Month'] = pd.to_datetime(extreme_events['Date']).dt.month
monthly_stats = pd.DataFrame({
    'Extreme_Weather_Days': extreme_events.groupby('Month').size(),
    'Safe_Fishing_Days': pd.Series(index=range(1,13), data=[31,28,31,30,31,30,31,31,30,31,30,31]) - extreme_events.groupby('Month').size()
})

# Calculate potential income impact
monthly_stats['Potential_Income_Loss'] = monthly_stats['Extreme_Weather_Days'] * (11000/30)  # Average daily income impact

# Visualize monthly patterns
plt.figure(figsize=(12, 6))
monthly_stats['Safe_Fishing_Days'].plot(kind='bar', color='green', label='Safe Fishing Days')
monthly_stats['Extreme_Weather_Days'].plot(kind='bar', color='red', alpha=0.5, label='Extreme Weather Days')
plt.title('Monthly Distribution of Safe vs Extreme Weather Days')
plt.xlabel('Month')
plt.ylabel('Days')
plt.legend()
plt.grid(True)
plt.show()

print("\
Monthly Analysis Summary:")
print(monthly_stats)

# Calculate annual statistics
annual_extreme_days = extreme_events['Month'].count()
annual_safe_days = 365 - annual_extreme_days
annual_income_loss = annual_extreme_days * (11000/30)

print("\
Annual Impact Summary:")
print(f"Total Extreme Weather Days: {annual_extreme_days}")
print(f"Total Safe Fishing Days: {annual_safe_days}")
print(f"Estimated Annual Income Loss: {annual_income_loss:.2f} INR")

