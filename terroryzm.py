import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('./DATA/globalterrorismdb_filtered.csv', encoding='ISO-8859-1')

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Extract year from the 'date' column and count the number of attacks per year
attacks_by_year = data['date'].dt.year.value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
attacks_by_year.plot(kind='line', color='skyblue')
plt.title('Terrorist Attacks by Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

