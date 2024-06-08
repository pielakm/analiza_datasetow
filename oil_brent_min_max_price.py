import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def oil_brent_min_max_price():
    # Wczytanie danych z pliku CSV
    data = pd.read_csv('./DATA/commodity_prices_filtered.csv')

    # Ekstrakcja kolumny z datą i ceną ropy Brent
    dates = pd.to_datetime(data['date'])
    oil_prices = data['oil_brent']

    # Znalezienie lokalnych maksimów i minimów
    peaks, _ = find_peaks(oil_prices)
    troughs, _ = find_peaks(-oil_prices)

    # Create a Figure
    fig, ax = plt.subplots(figsize=(14, 7))

    # Rysowanie wykresu
    ax.plot(dates, oil_prices, label='Cena ropy Brent')

    # Dodanie lokalnych maksimów i minimów
    ax.plot(dates[peaks], oil_prices[peaks], 'r^', label='Lokalne maksima')
    ax.plot(dates[troughs], oil_prices[troughs], 'gv', label='Lokalne minima')

    # Dodanie tytułu i etykiet osi
    ax.set_title('Cena ropy Brent z lokalnymi maksimami i minimami')
    ax.set_xlabel('Data')
    ax.set_ylabel('Cena (USD)')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    return fig

fig = oil_brent_min_max_price()
plt.show()
