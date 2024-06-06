# import xml.etree.ElementTree as ET
# import json
# import pandas as pd
# import matplotlib.pyplot as plt

# # Wczytywanie i przetwarzanie danych z pliku XML
# tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
# root = tree.getroot()

# # Tworzenie listy dat ataków w USA
# attack_dates = []

# for event in root.findall('event'):
#     country = event.find('country_txt').text
#     if country == 'United States':
#         date = event.find('date').text
#         attack_dates.append(date)

# # Konwersja listy dat ataków na DataFrame
# attack_df = pd.DataFrame(attack_dates, columns=['date'])
# attack_df['date'] = pd.to_datetime(attack_df['date'])
# attack_count = attack_df.groupby(attack_df['date'].dt.to_period('M')).size().reset_index(name='attack_count')

# # Wczytywanie i przetwarzanie danych z pliku JSON
# with open('./DATA/commodity_prices_filtered.json', 'r') as f:
#     commodity_prices = json.load(f)

# # Tworzenie DataFrame z danych o cenach surowców
# commodity_df = pd.DataFrame(commodity_prices)
# commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# # Filtrowanie kolumny 'oil_dubai' i grupowanie po miesiącach
# oil_df = commodity_df[['date', 'oil_dubai']]
# oil_df = oil_df.set_index('date').resample('M').mean().reset_index()

# # Łączenie danych na podstawie daty
# merged_df = pd.merge(oil_df, attack_count, on='date', how='left')
# merged_df['attack_count'] = merged_df['attack_count'].fillna(0)

# # Tworzenie wykresu
# fig, ax1 = plt.subplots()

# color = 'tab:blue'
# ax1.set_xlabel('Data')
# ax1.set_ylabel('Cena oil_dubai', color=color)
# ax1.plot(merged_df['date'], merged_df['oil_dubai'], color=color)
# ax1.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Liczba ataków', color=color)
# ax2.bar(merged_df['date'], merged_df['attack_count'], color=color, alpha=0.6)
# ax2.tick_params(axis='y', labelcolor=color)

# fig.tight_layout()
# plt.title('Zależność ceny oil_dubai do liczby ataków w United States')
# plt.show()

# # Analiza korelacji
# print(merged_df.corr())






# import xml.etree.ElementTree as ET
# import json
# import pandas as pd
# import matplotlib.pyplot as plt

# # Wczytywanie i przetwarzanie danych z pliku XML
# tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
# root = tree.getroot()

# # Tworzenie listy dat ataków w USA
# attack_dates = []

# for event in root.findall('event'):
#     country = event.find('country_txt').text
#     if country == 'United States':
#         date = event.find('date').text
#         attack_dates.append(date)

# # Konwersja listy dat ataków na DataFrame
# attack_df = pd.DataFrame(attack_dates, columns=['date'])
# attack_df['date'] = pd.to_datetime(attack_df['date'], errors='coerce')
# attack_df = attack_df.dropna()
# attack_count = attack_df.groupby(attack_df['date'].dt.year).size().reset_index(name='attack_count')

# # Wczytywanie i przetwarzanie danych z pliku JSON
# with open('./DATA/commodity_prices_filtered.json', 'r') as f:
#     commodity_prices = json.load(f)

# # Tworzenie DataFrame z danych o cenach surowców
# commodity_df = pd.DataFrame(commodity_prices)
# commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# # Filtrowanie kolumny 'oil_dubai' i grupowanie po latach
# oil_df = commodity_df[['date', 'oil_dubai']]
# oil_df = oil_df.set_index('date').resample('Y').mean().reset_index()

# # Łączenie danych na podstawie roku
# attack_count['date'] = pd.to_datetime(attack_count['date'], format='%Y')
# merged_df = pd.merge(oil_df, attack_count, on='date', how='left')
# merged_df['attack_count'] = merged_df['attack_count'].fillna(0)

# # Tworzenie wykresu
# fig, ax1 = plt.subplots()

# color = 'tab:blue'
# ax1.set_xlabel('Data')
# ax1.set_ylabel('Cena oil_dubai', color=color)
# ax1.plot(merged_df['date'], merged_df['oil_dubai'], color=color, label='Cena oil_dubai')
# ax1.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Liczba ataków', color=color)
# ax2.plot(merged_df['date'], merged_df['attack_count'], color=color, label='Liczba ataków')
# ax2.tick_params(axis='y', labelcolor=color)

# fig.tight_layout()
# plt.title('Zależność ceny oil_dubai do liczby ataków w United States')
# fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))
# plt.show()





import pandas as pd
import json
import matplotlib.pyplot as plt

# Load and process data from the CSV file
csv_file = './DATA/globalterrorismdb_filtered.csv'
terrorism_df = pd.read_csv(csv_file)
terrorism_df['date'] = pd.to_datetime(terrorism_df['date'], format='%Y-%m-%d')

# Filter data for attacks in the United States
us_attacks_df = terrorism_df[terrorism_df['country_txt'] == 'United States']

# Count attacks per year
attack_count = us_attacks_df.groupby(us_attacks_df['date'].dt.year).size().reset_index(name='attack_count')

# Load and process data from the JSON file
json_file = './DATA/commodity_prices_filtered.json'
with open(json_file, 'r') as f:
    commodity_prices = json.load(f)

# Create DataFrame from commodity prices data
commodity_df = pd.DataFrame(commodity_prices)
commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# Filter oil prices and group by year
oil_df = commodity_df[['date', 'oil_dubai']]
oil_df = oil_df.set_index('date').resample('Y').mean().reset_index()

# Merge datasets on the basis of year
merged_df = pd.merge(oil_df, attack_count, left_on=oil_df['date'].dt.year, right_on='date', how='left')
merged_df['attack_count'] = merged_df['attack_count'].fillna(0)

# Plotting
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Price of oil_dubai', color=color)
ax1.plot(merged_df['date'], merged_df['oil_dubai'], color=color, label='Price of oil_dubai')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Number of Attacks', color=color)
ax2.plot(merged_df['date'], merged_df['attack_count'], color=color, label='Number of Attacks')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Relationship between the price of oil_dubai and the number of attacks in the United States')
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))
plt.show()

