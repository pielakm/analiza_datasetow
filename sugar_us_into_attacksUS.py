import xml.etree.ElementTree as ET
import json
import pandas as pd
import matplotlib.pyplot as plt

# Wczytywanie i przetwarzanie danych z pliku XML
tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
root = tree.getroot()

# Tworzenie listy dat ataków w USA
attack_dates = []

for event in root.findall('event'):
    country = event.find('country_txt').text
    if country == 'United States':
        date = event.find('date').text
        attack_dates.append(date)

# Konwersja listy dat ataków na DataFrame
attack_df = pd.DataFrame(attack_dates, columns=['date'])
attack_df['date'] = pd.to_datetime(attack_df['date'])
attack_count = attack_df.groupby(attack_df['date'].dt.to_period('M')).size().reset_index(name='attack_count')

# Wczytywanie i przetwarzanie danych z pliku JSON
with open('./DATA/commodity_prices_filtered.json', 'r') as f:
    commodity_prices = json.load(f)

# Tworzenie DataFrame z danych o cenach surowców
commodity_df = pd.DataFrame(commodity_prices)
commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# Filtrowanie kolumny 'sugar_us' i grupowanie po miesiącach
sugar_df = commodity_df[['date', 'sugar_us']]
sugar_df = sugar_df.set_index('date').resample('M').mean().reset_index()

# Łączenie danych na podstawie daty
merged_df = pd.merge(sugar_df, attack_count, on='date', how='left')
merged_df['attack_count'] = merged_df['attack_count'].fillna(0)

# Tworzenie wykresu
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Data')
ax1.set_ylabel('Cena sugar_us', color=color)
ax1.plot(merged_df['date'], merged_df['sugar_us'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Liczba ataków', color=color)
ax2.bar(merged_df['date'], merged_df['attack_count'], color=color, alpha=0.6)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Zależność ceny sugar_us do liczby ataków w United States')
plt.show()

# Analiza korelacji
print(merged_df.corr())
