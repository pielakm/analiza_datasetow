import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
file_path = './DATA/commodity_prices_filtered.csv'
data = pd.read_csv(file_path)

# Konwersja kolumny 'date' na format daty
data['date'] = pd.to_datetime(data['date'])

# Wybierz kolumny 'date', 'tea_columbo', 'tea_kolkata' i 'tea_mombasa'
tea_data = data[['date', 'tea_columbo', 'tea_kolkata', 'tea_mombasa']]

# Generowanie wykresu
plt.figure(figsize=(12, 6))
plt.plot(tea_data['date'], tea_data['tea_columbo'], marker='o', linestyle='-', label='Tea Colombo', color='b', markersize=3)
plt.plot(tea_data['date'], tea_data['tea_kolkata'], marker='o', linestyle='-', label='Tea Kolkata', color='r', markersize=3)
plt.plot(tea_data['date'], tea_data['tea_mombasa'], marker='o', linestyle='-', label='Tea Mombasa', color='g', markersize=3)

# Dodanie legendy
plt.legend()

# Dodanie tytułu i etykiet osi
plt.title('Ceny różnych rodzajów herbat w czasie')
plt.xlabel('Data')
plt.ylabel('Cena herbaty')
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
