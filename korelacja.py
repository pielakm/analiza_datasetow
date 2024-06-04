import pandas as pd

# Load the dataset from XML file
data_terrorism = pd.read_xml('./DATA/globalterrorismdb_filtered.xml')

# Convert 'date' column to datetime type
data_terrorism['date'] = pd.to_datetime(data_terrorism['date'], format='%Y-%m-%d', errors='coerce')

# Extract year from the 'date' column and count the number of attacks per date
attacks_by_date = data_terrorism['date'].value_counts().sort_index().rename("attacks")

# Read the CSV file into a DataFrame
df_commodities = pd.read_csv("./DATA/commodity_prices_filtered.csv", index_col="date", parse_dates=True, encoding='latin-1')

# Prepare the oil price data
oil_prices = df_commodities["oil_dubai"].rename("oil_price")

# Merge the two datasets on the date index
merged_data = pd.concat([attacks_by_date, oil_prices], axis=1).fillna(0)

# Calculate the correlation between number of attacks and oil prices
correlations = merged_data['attacks'].rolling(window=30).corr(merged_data['oil_price'].shift(30)).dropna()

# Find the highest correlations
highest_correlations = correlations.abs().nlargest(5)

for date, correlation in highest_correlations.iteritems():
    print(f"Date of attack: {date}")
    print(f"Correlation: {correlation}")
    # Find the date when the oil price rose due to the attack (assuming a 30-day period)
    approximate_date_of_increase = date + pd.Timedelta(days=30)
    print(f"Approximate date of oil price increase: {approximate_date_of_increase}\n")

