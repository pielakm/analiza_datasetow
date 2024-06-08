# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns


# def sugar_eu_us_world_price():
#     # Wczytaj dane z JSON
#     with open('./DATA/commodity_prices_filtered.json') as f:
#         price_data = json.load(f)

#     df_prices = pd.DataFrame(price_data)
#     df_prices['date'] = pd.to_datetime(df_prices['date'])

#     # Wykres cen cukru w różnych regionach względem daty
#     plt.figure(figsize=(12, 6))
#     plt.plot(df_prices['date'], df_prices['sugar_eu'], marker='o', label='Sugar EU')
#     plt.plot(df_prices['date'], df_prices['sugar_us'], marker='o', label='Sugar US')
#     plt.plot(df_prices['date'], df_prices['sugar_world'], marker='o', label='Sugar World')
#     plt.title('Ceny cukru w różnych regionach w czasie')
#     plt.xlabel('Data')
#     plt.ylabel('Cena')
#     plt.legend()
#     plt.grid(True)
#     return plt
# # sugar_eu_us_world_price().show()

import json
import pandas as pd
import matplotlib.pyplot as plt

def sugar_eu_us_world_price():
    # Load data from JSON
    with open('./DATA/commodity_prices_filtered.json') as f:
        price_data = json.load(f)

    df_prices = pd.DataFrame(price_data)
    df_prices['date'] = pd.to_datetime(df_prices['date'])

    # Plot sugar prices in different regions over time
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_prices['date'], df_prices['sugar_eu'], marker='o', label='Sugar EU')
    ax.plot(df_prices['date'], df_prices['sugar_us'], marker='o', label='Sugar US')
    ax.plot(df_prices['date'], df_prices['sugar_world'], marker='o', label='Sugar World')
    ax.set_title('Sugar Prices in Different Regions Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)

    return fig

