import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load the dataset from XML file
data = pd.read_xml('./DATA/globalterrorismdb_filtered.xml')

# Check the first few rows to understand the structure
print(data.head())

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d', errors='coerce')

# Extract year from the 'date' column and count the number of attacks per year
attacks_by_year = data['date'].dt.year.value_counts().sort_index().astype(int)

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=attacks_by_year, label='Data', color='blue')
plt.title('Terrorist Attacks by Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')

# Set major ticks format to show every year
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

# Find maximum and minimum values
max_value = attacks_by_year.max()
min_value = attacks_by_year.min()

# Find years for maximum and minimum values
max_year = attacks_by_year.idxmax()
min_year = attacks_by_year.idxmin()

# Mark the maximum and minimum points on the plot
plt.scatter(max_year, max_value, color='r', s=100, zorder=5, label=f'Maximum: {max_value} in {max_year}')
plt.scatter(min_year, min_value, color='g', s=100, zorder=5, label=f'Minimum: {min_value} in {min_year}')

plt.tight_layout()
plt.legend()
plt.show()
