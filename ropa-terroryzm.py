import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load the dataset from XML file
data_terrorism = pd.read_xml('./DATA/globalterrorismdb_filtered.xml')

# Convert 'date' column to datetime type
data_terrorism['date'] = pd.to_datetime(data_terrorism['date'], format='%Y-%m-%d', errors='coerce')

# Extract year from the 'date' column and count the number of attacks per date
attacks_by_date = data_terrorism['date'].value_counts().sort_index().rename("attacks")

# Read the CSV file into a DataFrame
df_commodities = pd.read_csv("./DATA/commodity_prices_filtered.csv", index_col="date", parse_dates=True, encoding='latin-1')

# Prepare the oil price data
oil_prices = df_commodities["oil_dubai"].rename("oil_price")

# Merge the two datasets on the date index
merged_data = pd.concat([attacks_by_date, oil_prices], axis=1).fillna(0)

# Plotting
plt.figure(figsize=(15, 6))

# Plot number of attacks
sns.lineplot(data=merged_data['attacks'], label='Number of Attacks', color='blue')

# Plot oil prices
sns.lineplot(data=merged_data['oil_price'], label='Dubai Oil Price', color='orange')

# Titles and labels
plt.title('Number of Terrorist Attacks and Dubai Oil Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Values')

# Set major ticks format to show every year
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Find maximum and minimum values for attacks
max_value_attacks = merged_data['attacks'].max()
min_value_attacks = merged_data['attacks'].min()

# Find dates for maximum and minimum values for attacks
max_date_attacks = merged_data['attacks'].idxmax()
min_date_attacks = merged_data['attacks'].idxmin()

# Mark the maximum and minimum points on the plot for attacks
plt.scatter(max_date_attacks, max_value_attacks, color='r', s=30, zorder=5, label=f'Max Attacks: {max_value_attacks} on {max_date_attacks.date()}')
plt.scatter(min_date_attacks, min_value_attacks, color='g', s=30, zorder=5, label=f'Min Attacks: {min_value_attacks} on {min_date_attacks.date()}')

# Find maximum and minimum values for oil prices
max_value_oil = merged_data['oil_price'].max()
min_value_oil = merged_data['oil_price'].min()

# Find dates for maximum and minimum values for oil prices
max_date_oil = merged_data['oil_price'].idxmax()
min_date_oil = merged_data['oil_price'].idxmin()

# Mark the maximum and minimum points on the plot for oil prices
plt.scatter(max_date_oil, max_value_oil, color='red', s=30, zorder=5, label=f'Max Oil Price: {max_value_oil:.2f} on {max_date_oil.date()}')
plt.scatter(min_date_oil, min_value_oil, color='green', s=30, zorder=5, label=f'Min Oil Price: {min_value_oil:.2f} on {min_date_oil.date()}')

# Show legend
plt.legend(loc='best')

plt.tight_layout()
plt.show()
