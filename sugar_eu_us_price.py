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

    print(f'Minimum price difference: {min_diff:.2f} USD (Date: {min_diff_date.date()})')
    print(f'Maximum price difference: {max_diff:.2f} USD (Date: {max_diff_date.date()})')
    
    # Plot sugar prices in the US and EU over time
    plt.figure(figsize=(12, 6))
    plt.plot(df_prices['date'], df_prices['sugar_us'], marker='o', label='Sugar price in US')
    plt.plot(df_prices['date'], df_prices['sugar_eu'], marker='o', label='Sugar price in EU')
    plt.title('Sugar Prices in the US and EU Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sugar Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot price differences over time
    plt.figure(figsize=(12, 6))
    plt.plot(df_prices['date'], df_prices['price_diff'], marker='o', label='Sugar Price Difference (US - EU)')
    plt.title('Sugar Price Differences between the US and EU Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price Difference (USD)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Call the function to execute the code
sugar_eu_us_price()
