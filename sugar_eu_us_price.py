# import json
# import pandas as pd
# import matplotlib.pyplot as plt


# def sugar_eu_us_price():
#     # Wczytaj dane z JSON
#     with open('./DATA/commodity_prices_filtered.json') as f:
#         price_data = json.load(f)

#     df_prices = pd.DataFrame(price_data)
#     df_prices['date'] = pd.to_datetime(df_prices['date'])
#     df_prices['year'] = df_prices['date'].dt.year
#     # Oblicz różnicę cenową między sugar_us a sugar_eu
#     df_prices['price_diff'] = df_prices['sugar_us'] - df_prices['sugar_eu']

#     # Wyznacz minimalną i maksymalną różnicę cenową
#     min_diff = df_prices['price_diff'].min()
#     max_diff = df_prices['price_diff'].max()
#     min_diff_date = df_prices.loc[df_prices['price_diff'].idxmin(), 'date']
#     max_diff_date = df_prices.loc[df_prices['price_diff'].idxmax(), 'date']

#     print(f'Minimalna różnica cenowa: {min_diff} USD (Data: {min_diff_date})')
#     print(f'Maksymalna różnica cenowa: {max_diff} USD (Data: {max_diff_date})')
#     # Wykres cen cukru w USA i UE w czasie
#     plt.figure(figsize=(12, 6))
#     plt.plot(df_prices['date'], df_prices['sugar_us'], marker='o', label='Cena cukru w USA')
#     plt.plot(df_prices['date'], df_prices['sugar_eu'], marker='o', label='Cena cukru w UE')
#     plt.title('Ceny cukru w USA i UE w czasie')
#     plt.xlabel('Data')
#     plt.ylabel('Cena cukru (USD)')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

#     # Wykres różnic cenowych w czasie
#     plt.figure(figsize=(12, 6))
#     plt.plot(df_prices['date'], df_prices['price_diff'], marker='o', label='Różnica cen cukru (USA - UE)')
#     plt.title('Różnice cen cukru między USA i UE w czasie')
#     plt.xlabel('Data')
#     plt.ylabel('Różnica cen (USD)')
#     plt.grid(True)
#     plt.legend()
#     return plt
# # sugar_eu_us_price().show()

import json
import pandas as pd
import matplotlib.pyplot as plt


def sugar_eu_us_price():
    # Load data from JSON
    with open('./DATA/commodity_prices_filtered.json') as f:
        price_data = json.load(f)

    df_prices = pd.DataFrame(price_data)
    df_prices['date'] = pd.to_datetime(df_prices['date'])
    df_prices['year'] = df_prices['date'].dt.year

    # Calculate the price difference between sugar_us and sugar_eu
    df_prices['price_diff'] = df_prices['sugar_us'] - df_prices['sugar_eu']

    # Determine the minimum and maximum price difference
    min_diff = df_prices['price_diff'].min()
    max_diff = df_prices['price_diff'].max()
    min_diff_date = df_prices.loc[df_prices['price_diff'].idxmin(), 'date']
    max_diff_date = df_prices.loc[df_prices['price_diff'].idxmax(), 'date']

    # Plot sugar prices in the US and EU over time
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_prices['date'], df_prices['sugar_us'], marker='o', label='Sugar price in US')
    ax1.plot(df_prices['date'], df_prices['sugar_eu'], marker='o', label='Sugar price in EU')
    ax1.set_title('Sugar Prices in the US and EU Over Time')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sugar Price (USD)')
    ax1.legend()
    ax1.grid(True)

    # Plot price differences over time
    fig, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(df_prices['date'], df_prices['price_diff'], marker='o', label='Sugar Price Difference (US - EU)')
    ax2.set_title('Sugar Price Differences between the US and EU Over Time')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Price Difference (USD)')
    ax2.grid(True)
    ax2.legend()

    return fig




