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
plt.plot(commodity_df['date'], commodity_df['coffee_arabica'], marker='o', linestyle='-', color='b')

# Dodanie tytułu i etykiet osi
plt.title('Cena kawy arabica na przestrzeni lat')
plt.xlabel('Data')
plt.ylabel('Cena kawy arabica ($ per lb)')

# Ustawienia siatki
plt.grid(True)

# Pokaż wykres
plt.show()
