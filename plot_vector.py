import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('lifeTime_mean.csv', delimiter=',', encoding="utf-8-sig")
print(df)
# Extract the confidence interval data
mean = df['Mean']
min_confint_t95 = df['Min_ConfInt_t95']
max_confint_t95 = df['Max_ConfInt_t95']
min_confint_t90 = df['Min_ConfInt_t90']
max_confint_t90 = df['Max_ConfInt_t90']

# Create the plot
plt.figure(figsize=(10, 6))
plt.errorbar(mean.index, mean, yerr=[mean - min_confint_t95, max_confint_t95 - mean],
             fmt='o', markersize=7, capsize=3, label='ConfInt t95')
plt.errorbar(mean.index, mean, yerr=[mean - min_confint_t90, max_confint_t90 - mean],
             fmt='o', markersize=5, capsize=3, label='ConfInt t90')

# Customize the plot
plt.xlabel('Mean')
plt.ylabel('Value (ms)')
plt.title('Mean Confidence Intervals')
plt.legend()

# Increase spacing between x-values
tick_spacing = 5  # Adjust the spacing as needed
tick_locations = np.arange(0, len(mean), tick_spacing)
plt.xticks(tick_locations, mean.index[tick_locations])


# Show the plot
plt.show()








