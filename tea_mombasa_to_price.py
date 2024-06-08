# import pandas as pd
# import matplotlib.pyplot as plt

# # Wczytaj dane z pliku CSV
# file_path = './DATA/commodity_prices_filtered.csv'
# data = pd.read_csv(file_path)

# # Konwersja kolumny 'date' na format daty
# data['date'] = pd.to_datetime(data['date'])

# # Wybierz kolumny 'date' i 'tea_mombasa'
# tea_mombasa_data = data[['date', 'tea_mombasa']]

# # Znajdź maksymalną i minimalną cenę
# max_price = tea_mombasa_data['tea_mombasa'].max()
# min_price = tea_mombasa_data['tea_mombasa'].min()
# max_date = tea_mombasa_data[tea_mombasa_data['tea_mombasa'] == max_price]['date'].iloc[0]
# min_date = tea_mombasa_data[tea_mombasa_data['tea_mombasa'] == min_price]['date'].iloc[0]

# # Generowanie wykresu
# plt.figure(figsize=(10, 5))
# plt.plot(tea_mombasa_data['date'], tea_mombasa_data['tea_mombasa'], marker='o', linestyle='-', color='b', label='Tea Mombasa Price', markersize=3)

# # Zaznacz maksymalną cenę
# plt.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
# plt.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

# # Zaznacz minimalną cenę
# plt.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
# plt.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

# plt.title('Price of Tea Mombasa Over Time')
# plt.xlabel('Date')
# plt.ylabel('Price of Tea Mombasa')
# plt.legend()
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = './DATA/commodity_prices_filtered.csv'
data = pd.read_csv(file_path)

def tea_mombasa_to_price():
    # Convert the 'date' column to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Select columns 'date' and 'tea_mombasa'
    tea_mombasa_data = data[['date', 'tea_mombasa']]

    # Find the maximum and minimum prices
    max_price = tea_mombasa_data['tea_mombasa'].max()
    min_price = tea_mombasa_data['tea_mombasa'].min()
    max_date = tea_mombasa_data[tea_mombasa_data['tea_mombasa'] == max_price]['date'].iloc[0]
    min_date = tea_mombasa_data[tea_mombasa_data['tea_mombasa'] == min_price]['date'].iloc[0]

    # Generate the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(tea_mombasa_data['date'], tea_mombasa_data['tea_mombasa'], marker='o', linestyle='-', color='b', label='Tea Mombasa Price', markersize=3)

    # Mark the maximum price
    ax.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
    ax.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

    # Mark the minimum price
    ax.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
    ax.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

    ax.set_title('Price of Tea Mombasa Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price of Tea Mombasa')
    ax.legend()
    ax.grid(True)

    # Return the figure object
    plt.close(fig)  # Close the plot to prevent automatic display
    return fig
