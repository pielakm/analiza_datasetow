import pandas as pd
import matplotlib.pyplot as plt


def tea_to_price():
    # Wczytaj dane z pliku CSV
    file_path = './DATA/commodity_prices_filtered.csv'
    data = pd.read_csv(file_path)

    # Konwersja kolumny 'date' na format daty
    data['date'] = pd.to_datetime(data['date'])

    # Wybierz kolumny 'date', 'tea_columbo', 'tea_kolkata' i 'tea_mombasa'
    tea_data = data[['date', 'tea_columbo', 'tea_kolkata', 'tea_mombasa']]

    # Generowanie wykresu
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tea_data['date'], tea_data['tea_columbo'], marker='o', linestyle='-', label='Tea Colombo', color='b', markersize=3)
    ax.plot(tea_data['date'], tea_data['tea_kolkata'], marker='o', linestyle='-', label='Tea Kolkata', color='r', markersize=3)
    ax.plot(tea_data['date'], tea_data['tea_mombasa'], marker='o', linestyle='-', label='Tea Mombasa', color='g', markersize=3)

    # Dodanie legendy
    ax.legend()

    # Dodanie tytułu i etykiet osi
    ax.set_title('Prices of Different Types of Tea Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price of Tea')
    ax.grid(True)

    plt.close()  # Close the plot to avoid displaying it immediately

    return fig

