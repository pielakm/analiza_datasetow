# import pandas as pd
# import matplotlib.pyplot as plt

# # Wczytaj dane z pliku CSV
# file_path = './DATA/commodity_prices_filtered.csv'
# data = pd.read_csv(file_path)

# # Konwersja kolumny 'date' na format daty
# data['date'] = pd.to_datetime(data['date'])

# # Wybierz kolumny 'date' i 'tea_columbo'
# tea_columbo_data = data[['date', 'tea_columbo']]

# # Znajdź maksymalną i minimalną cenę
# max_price = tea_columbo_data['tea_columbo'].max()
# min_price = tea_columbo_data['tea_columbo'].min()
# max_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == max_price]['date'].iloc[0]
# min_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == min_price]['date'].iloc[0]

# # Generowanie wykresu
# plt.figure(figsize=(10, 5))
# plt.plot(tea_columbo_data['date'], tea_columbo_data['tea_columbo'], marker='o', linestyle='-', color='b', label='Tea Columbo Price', markersize=3)

# # Zaznacz maksymalną cenę
# plt.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
# plt.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

# # Zaznacz minimalną cenę
# plt.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
# plt.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

# plt.title('Price of Tea Columbo Over Time')
# plt.xlabel('Date')
# plt.ylabel('Price of Tea Columbo')
# plt.legend()
# plt.grid(True)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = './DATA/commodity_prices_filtered.csv'
data = pd.read_csv(file_path)

def tea_columbo_to_price():
    # Convert the 'date' column to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Select columns 'date' and 'tea_columbo'
    tea_columbo_data = data[['date', 'tea_columbo']]

    # Find the maximum and minimum prices
    max_price = tea_columbo_data['tea_columbo'].max()
    min_price = tea_columbo_data['tea_columbo'].min()
    max_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == max_price]['date'].iloc[0]
    min_date = tea_columbo_data[tea_columbo_data['tea_columbo'] == min_price]['date'].iloc[0]

    # Generate the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(tea_columbo_data['date'], tea_columbo_data['tea_columbo'], marker='o', linestyle='-', color='b', label='Tea Columbo Price', markersize=3)

    # Mark the maximum price
    ax.scatter(max_date, max_price, color='r', label=f'Max Price: {max_price} on {max_date.date()}')
    ax.text(max_date, max_price, f'{max_price:.2f}', fontsize=12, verticalalignment='bottom', color='r')

    # Mark the minimum price
    ax.scatter(min_date, min_price, color='g', label=f'Min Price: {min_price} on {min_date.date()}')
    ax.text(min_date, min_price, f'{min_price:.2f}', fontsize=12, verticalalignment='top', color='g')

    ax.set_title('Price of Tea Columbo Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price of Tea Columbo')
    ax.legend()
    ax.grid(True)

    # Return the figure object
    plt.close(fig)  # Close the plot to prevent automatic display
    return fig


