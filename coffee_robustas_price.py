# import pandas as pd
# import json
# import matplotlib.pyplot as plt

# # Załaduj dane z pliku JSON
# json_file = './DATA/commodity_prices_filtered.json'
# with open(json_file, 'r') as f:
#     commodity_prices = json.load(f)

# # Utwórz DataFrame z danych
# commodity_df = pd.DataFrame(commodity_prices)
# commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# # Sortuj dane według daty
# commodity_df = commodity_df.sort_values(by='date')

# # Rysowanie wykresu
# plt.figure(figsize=(10, 6))
# plt.plot(commodity_df['date'], commodity_df['coffee_robustas'], marker='o', linestyle='-', color='b')

# # Dodanie tytułu i etykiet osi
# plt.title('Cena kawy robustas na przestrzeni lat')
# plt.xlabel('Data')
# plt.ylabel('Cena kawy robustas ($ per lb)')

# # Ustawienia siatki
# plt.grid(True)

# # Pokaż wykres
# plt.show()
import pandas as pd
import json
import matplotlib.pyplot as plt

# Załaduj dane z pliku JSON
json_file = './DATA/commodity_prices_filtered.json'
with open(json_file, 'r') as f:
    commodity_prices = json.load(f)

# Utwórz DataFrame z danych
commodity_df = pd.DataFrame(commodity_prices)
commodity_df['date'] = pd.to_datetime(commodity_df['date'])

# Sortuj dane według daty
commodity_df = commodity_df.sort_values(by='date')

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(commodity_df['date'], commodity_df['coffee_robustas'], marker='o', linestyle='-', color='b')

# Dodanie tytułu i etykiet osi
plt.title('Cena kawy robustas na przestrzeni lat')
plt.xlabel('Data')
plt.ylabel('Cena kawy robustas ($ per lb)')

# Ustawienia siatki
plt.grid(True)

# Dodanie minimalnej i maksymalnej ceny na wykresie
min_price = commodity_df['coffee_robustas'].min()
max_price = commodity_df['coffee_robustas'].max()
plt.axhline(y=min_price, color='r', linestyle='--', label=f'Min cena: ${min_price:.2f}')
plt.axhline(y=max_price, color='g', linestyle='--', label=f'Max cena: ${max_price:.2f}')
plt.legend()

# Pokaż wykres
plt.show()
