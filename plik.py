import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the JSON file into a DataFrame
with open("./DATA/commodity_prices_filtered.json", "r") as file:
    data = json.load(file)
df = pd.DataFrame(data)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set 'date' column as index
df.set_index('date', inplace=True)

# Plot oil_dubai prices against dates
plt.figure(figsize=(15, 5))
oil_plot = sns.lineplot(data=df["oil_dubai"].rolling(20).mean())  # Rolling mean for smoothing, if desired
plt.title("Dubai Oil Prices")
plt.ylabel("Price per Barrel (USD)")
plt.xlabel("Year")

# Set x-axis to display years at 5-year intervals
plt.xticks(pd.date_range(start=df.index.min(), end=df.index.max(), freq='5Y').strftime('%Y'))

# Find maximum and minimum values
max_value = df["oil_dubai"].max()
min_value = df["oil_dubai"].min()

# Draw lines for max and min values
plt.axhline(y=max_value, color='r', linestyle='--', label=f'Maximum: {max_value:.2f}')
plt.axhline(y=min_value, color='g', linestyle='--', label=f'Minimum: {min_value:.2f}')

# Show legend
plt.legend()

plt.show()