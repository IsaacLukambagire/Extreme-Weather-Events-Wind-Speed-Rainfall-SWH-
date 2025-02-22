#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Redefine X_2025 for predictions
X_2025 = pd.DataFrame({
    'DayOfYear': [d.timetuple().tm_yday for d in dates_2025],
    'Month': [d.month for d in dates_2025]
})

# Generate predictions for 2025
predictions_cleaned = pd.DataFrame()
predictions_cleaned['Date'] = dates_2025
for target in targets:
    predictions_cleaned[target] = rf_models_cleaned[target].predict(X_2025)

# Plot predictions
plt.figure(figsize=(15, 10))
for i, target in enumerate(targets, 1):
    plt.subplot(3, 1, i)
    plt.plot(predictions_cleaned['Date'], predictions_cleaned[target], label='Predicted')
    plt.title(f'Predicted {target} for 2025')
    plt.xlabel('Date')
    plt.ylabel(target)
    plt.grid(True)
plt.tight_layout()
plt.show()

# Save predictions to CSV
predictions_cleaned.to_csv('weather_predictions_2025_cleaned.csv', index=False)
print('Predictions saved to weather_predictions_2025_cleaned.csv')

# Show summary statistics of predictions
print('\
Prediction Summary Statistics:')
print(predictions_cleaned[targets].describe())

