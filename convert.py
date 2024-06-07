import pandas as pd

# data prices
data_prices = pd.read_csv('commodity_prices.csv', encoding='utf-8')
data_prices['date'] = pd.to_datetime(data_prices['date'])
data_prices = data_prices[data_prices['date'] >= '1970-01-01'].copy()
data_prices = data_prices[data_prices['date'] <= '2015-12-31'].copy()
data_prices['priceid'] = range(1, len(data_prices) + 1)
data_prices.to_csv('commodity_prices_filtered.csv', index=False)

# data terror
data_terror = pd.read_csv('./DATA/globalterrorismdb_filtered.csv', encoding='ISO-8859-1', low_memory=False)
data_terror['date'] = data_terror['iyear'].astype(str) + '-' + data_terror['imonth'].astype(str) + '-' + data_terror['iday'].astype(str)
data_terror = data_terror[data_terror['date'] >= '1970-01-01'].copy()
data_terror = data_terror[data_terror['date'] <= '2015-12-31'].copy()
data_terror = data_terror[['country_txt', 'region_txt','city', 'date']]
data_terror['eventid'] = range(1, len(data_terror) + 1)
data_terror.to_csv('globalterrorismdb_filtered2.csv', index=False)