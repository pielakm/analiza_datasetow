import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Wczytanie danych z pliku CSV
data = pd.read_csv('commodity_prices_filtered.csv')

# Ekstrakcja kolumny z datą i ceną ropy Brent
dates = pd.to_datetime(data['date'])
oil_prices = data['oil_brent']

# Znalezienie lokalnych maksimów i minimów
peaks, _ = find_peaks(oil_prices)
troughs, _ = find_peaks(-oil_prices)

# Rysowanie wykresu
plt.figure(figsize=(14, 7))
plt.plot(dates, oil_prices, label='Cena ropy Brent')

# Dodanie lokalnych maksimów i minimów
plt.plot(dates[peaks], oil_prices[peaks], 'r^', label='Lokalne maksima')
plt.plot(dates[troughs], oil_prices[troughs], 'gv', label='Lokalne minima')

# Dodanie tytułu i etykiet osi
plt.title('Cena ropy Brent z lokalnymi maksimami i minimami')
plt.xlabel('Data')
plt.ylabel('Cena (USD)')
plt.legend()
plt.grid(True)

# Wyświetlenie wykresu
plt.show()

