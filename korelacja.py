import pandas as pd

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

# Calculate the correlation between number of attacks and oil prices
correlations = merged_data['attacks'].rolling(window=30).corr(merged_data['oil_price'].shift(30)).dropna()

# Find the highest correlations
highest_correlations = correlations.abs().nlargest(5)

for date, correlation in highest_correlations.items():
    print(f"Date of attack: {date}")
    print(f"Correlation: {correlation}")
    # Find the date when the oil price rose due to the attack (assuming a 30-day period)
    approximate_date_of_increase = date + pd.Timedelta(days=365)
    print(f"Approximate date of oil price increase: {approximate_date_of_increase}\n")

# import xml.etree.ElementTree as ET
# import pandas as pd

# # Wczytaj dane z XML
# tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
# root = tree.getroot()

# # Wyodrębnij dane do DataFrame
# conflict_data = []
# for event in root.findall('event'):
#     date = event.find('date').text
#     year = date.split('-')[0]
#     conflict_data.append({'year': year})

# df_conflicts = pd.DataFrame(conflict_data)
# df_conflicts['year'] = df_conflicts['year'].astype(int)

# # Policz liczbę ataków w każdym roku
# conflict_counts = df_conflicts['year'].value_counts().sort_index().reset_index()
# conflict_counts.columns = ['year', 'num_attacks']
# import json

# # Wczytaj dane z JSON
# with open('./DATA/commodity_prices_filtered.json') as f:
#     price_data = json.load(f)

# df_prices = pd.DataFrame(price_data)
# df_prices['date'] = pd.to_datetime(df_prices['date'])
# df_prices['year'] = df_prices['date'].dt.year

# # Połącz dane
# df_combined = pd.merge(conflict_counts, df_prices, on='year')

# # Analiza korelacji
# correlation_matrix = df_combined.corr()
# print(correlation_matrix[['num_attacks']])

# import matplotlib.pyplot as plt

# # Wykres liczby ataków w czasie
# plt.figure(figsize=(12, 6))
# plt.plot(conflict_counts['year'], conflict_counts['num_attacks'], marker='o')
# plt.title('Liczba ataków w czasie')
# plt.xlabel('Rok')
# plt.ylabel('Liczba ataków')
# plt.grid(True)
# plt.show()

# # Wykres cen surowców w czasie
# plt.figure(figsize=(12, 6))
# for column in df_prices.columns[1:]:
#     plt.plot(df_prices['year'], df_prices[column], marker='o', label=column)
# plt.title('Ceny surowców w czasie')
# plt.xlabel('Rok')
# plt.ylabel('Cena')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Wykres korelacji
# plt.figure(figsize=(12, 6))
# plt.scatter(df_combined['num_attacks'], df_combined['oil_brent'], label='Oil Brent')
# plt.scatter(df_combined['num_attacks'], df_combined['coffee_arabica'], label='Coffee Arabica')
# plt.title('Korelacja między liczbą ataków a cenami surowców')
# plt.xlabel('Liczba ataków')
# plt.ylabel('Cena')
# plt.legend()
# plt.grid(True)
# plt.show()

