import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv("./DATA/commodity_prices_filtered.csv", index_col="date", parse_dates=True, encoding='latin-1')

# Plot oil_dubai prices against dates
plt.figure(figsize=(15, 5))
oil_plot = sns.lineplot(data=df["oil_dubai"].rolling(20).mean())  # Rolling mean for smoothing, if desired
plt.title("Dubai Oil Prices")
plt.ylabel("Price per Barrel (USD)")
plt.xlabel("Date")

# Find maximum and minimum values
max_value = df["oil_dubai"].max()
min_value = df["oil_dubai"].min()

# Draw lines for max and min values
plt.axhline(y=max_value, color='r', linestyle='--', label=f'Maximum: {max_value:.2f}')
plt.axhline(y=min_value, color='g', linestyle='--', label=f'Minimum: {min_value:.2f}')

# Show legend
plt.legend()

plt.show()
