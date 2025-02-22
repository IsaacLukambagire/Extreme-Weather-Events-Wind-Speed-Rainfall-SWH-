#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Calculate correlations between parameters
correlation_matrix = df[['Rainfall', 'Wind_Speed (m/s)', 'SWH']].corr()

# Visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Weather Parameters')
plt.show()

# Analyze trends over specific years or seasons
# Extract year and season information
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Season'] = np.where(df['Month'].isin([12, 1, 2]), 'Winter',
                        np.where(df['Month'].isin([3, 4, 5]), 'Spring',
                                 np.where(df['Month'].isin([6, 7, 8]), 'Summer', 'Fall')))

# Group by year and season to analyze trends
seasonal_trends = df.groupby(['Year', 'Season'])[['Rainfall', 'Wind_Speed (m/s)', 'SWH']].mean()

# Visualize seasonal trends
seasonal_trends.unstack().plot(kind='line', figsize=(12, 6))
plt.title('Seasonal Trends of Weather Parameters Over Time')
plt.ylabel('Average Values')
plt.xlabel('Year')
plt.legend(title='Parameter and Season', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

