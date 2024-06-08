import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
file_path = './DATA/commodity_prices_filtered.csv'
data = pd.read_csv(file_path)

# Konwersja kolumny 'date' na format daty
data['date'] = pd.to_datetime(data['date'])

# Wybierz kolumny 'date' i 'tea_kolkata'
tea_kolkata_data = data[['date', 'tea_kolkata']]

# Znajdź maksymalną i minimalną cenę
max_price = tea_kolkata_data['tea_kolkata'].max()
min_price = tea_kolkata_data['tea_kolkata'].min()
max_date = tea_kolkata_data[tea_kolkata_data['tea_kolkata'] == max_price]['date'].iloc[0]
min_date = tea_kolkata_data[tea_kolkata_data['tea_kolkata'] == min_price]['date'].iloc[0]

# Generowanie wykresu
plt.figure(figsize=(10, 5))
plt.plot(tea_kolkata_data['date'], tea_kolkata_data['tea_kolkata'], marker='o', linestyle='-', color='b', label='Tea Kolkata Price', markersize=3)

# Zaznacz maksymalną cenę
plt.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
plt.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

# Zaznacz minimalną cenę
plt.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
plt.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

plt.title('Price of Tea Kolkata Over Time')
plt.xlabel('Date')
plt.ylabel('Price of Tea Kolkata')
plt.legend()
plt.grid(True)
plt.show()