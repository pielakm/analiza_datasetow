import xml.etree.ElementTree as ET
import pandas as pd

# Wczytaj dane z XML
tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
root = tree.getroot()

# Wyodrębnij dane do DataFrame
conflict_data = []
for event in root.findall('event'):
    date = event.find('date').text
    year = date.split('-')[0]
    conflict_data.append({'year': year})

df_conflicts = pd.DataFrame(conflict_data)
df_conflicts['year'] = df_conflicts['year'].astype(int)

# Policz liczbę ataków w każdym roku
conflict_counts = df_conflicts['year'].value_counts().sort_index().reset_index()
conflict_counts.columns = ['year', 'num_attacks']
import json

# Wczytaj dane z JSON
with open('./DATA/commodity_prices_filtered.json') as f:
    price_data = json.load(f)

df_prices = pd.DataFrame(price_data)
df_prices['date'] = pd.to_datetime(df_prices['date'])
df_prices['year'] = df_prices['date'].dt.year
# Połącz dane na podstawie roku
df_combined = pd.merge(conflict_counts, df_prices[['year', 'sugar_us']], on='year')
# Analiza korelacji
correlation = df_combined['num_attacks'].corr(df_combined['sugar_us'])
print(f'Korelacja między liczbą ataków a ceną cukru w USA: {correlation}')
import matplotlib.pyplot as plt

# Wykres liczby ataków w czasie
plt.figure(figsize=(12, 6))
plt.plot(conflict_counts['year'], conflict_counts['num_attacks'], marker='o', label='Liczba ataków')
plt.title('Liczba ataków w czasie')
plt.xlabel('Rok')
plt.ylabel('Liczba ataków')
plt.grid(True)
plt.legend()
plt.show()

# Wykres cen cukru w USA w czasie
plt.figure(figsize=(12, 6))
plt.plot(df_prices['year'], df_prices['sugar_us'], marker='o', label='Cena cukru w USA')
plt.title('Cena cukru w USA w czasie')
plt.xlabel('Rok')
plt.ylabel('Cena cukru w USD')
plt.grid(True)
plt.legend()
plt.show()

# Wykres zależności między liczbą ataków a ceną cukru w USA
plt.figure(figsize=(12, 6))
plt.scatter(df_combined['num_attacks'], df_combined['sugar_us'], marker='o')
plt.title('Zależność między liczbą ataków a ceną cukru w USA')
plt.xlabel('Liczba ataków')
plt.ylabel('Cena cukru w USD')
plt.grid(True)
plt.show()
