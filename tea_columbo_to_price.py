import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
file_path = './DATA/commodity_prices_filtered.csv'
data = pd.read_csv(file_path)

# Konwersja kolumny 'date' na format daty
data['date'] = pd.to_datetime(data['date'])

# Wybierz kolumny 'date' i 'tea_columbo'
tea_columbo_data = data[['date', 'tea_columbo']]

# Znajdź maksymalną i minimalną cenę
max_price = tea_columbo_data['tea_columbo'].max()
min_price = tea_columbo_data['tea_columbo'].min()
max_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == max_price]['date'].iloc[0]
min_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == min_price]['date'].iloc[0]

# Generowanie wykresu
plt.figure(figsize=(10, 5))
plt.plot(tea_columbo_data['date'], tea_columbo_data['tea_columbo'], marker='o', linestyle='-', color='b', label='Tea Columbo Price', markersize=3)

# Zaznacz maksymalną cenę
plt.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
plt.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

# Zaznacz minimalną cenę
plt.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
plt.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

plt.title('Cena Tea Columbo w czasie')
plt.xlabel('Data')
plt.ylabel('Cena Tea Columbo')
plt.legend()
plt.grid(True)
plt.show()