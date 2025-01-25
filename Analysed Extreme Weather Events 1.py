#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('Weather_Parameters_Combined.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Define thresholds
RAINFALL_THRESHOLD = 20.1  # mm/h
WIND_SPEED_THRESHOLD = 5.57  # m/s
SWH_THRESHOLD = 2.1  # meters

# Find extreme weather days
extreme_days = df[
    (df['Rainfall'] >= RAINFALL_THRESHOLD) |
    (df['Wind_Speed (m/s)'] >= WIND_SPEED_THRESHOLD) |
    (df['SWH'] >= SWH_THRESHOLD)
]

# Calculate percentage of extreme days
total_days = len(df)
extreme_days_count = len(extreme_days)
extreme_percentage = (extreme_days_count / total_days) * 100

print('Summary of Extreme Weather Analysis:')
print('Total number of days in dataset:', total_days)
print('Number of extreme weather days:', extreme_days_count)
print('Percentage of extreme weather days: {:.2f}%'.format(extreme_percentage))

# Count individual threshold exceedances
rainfall_extremes = len(df[df['Rainfall'] >= RAINFALL_THRESHOLD])
wind_extremes = len(df[df['Wind_Speed (m/s)'] >= WIND_SPEED_THRESHOLD])
swh_extremes = len(df[df['SWH'] >= SWH_THRESHOLD])

print('\
Breakdown of extreme events:')
print('Days with extreme rainfall (>=20.1 mm/h):', rainfall_extremes)
print('Days with extreme wind speed (>=5.57 m/s):', wind_extremes)
print('Days with extreme wave height (>=2.1 m):', swh_extremes)

# Create a visualization of extreme events by month
extreme_days['Month'] = extreme_days['Date'].dt.month
monthly_counts = extreme_days['Month'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
monthly_counts.plot(kind='bar')
plt.title('Distribution of Extreme Weather Days by Month')
plt.xlabel('Month')
plt.ylabel('Number of Extreme Weather Days')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.tight_layout()
plt.show()

