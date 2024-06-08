
import pandas as pd
import json
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET


# Function to parse dates safely
def safe_parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
    except ValueError:
        return None


def oil_dubai_to_attacksUSA():
    # Load and process data from the XML file
    xml_file = './DATA/globalterrorismdb_filtered.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract relevant data from the XML
    data = []
    for event in root.findall('event'):
        country = event.find('country_txt').text
        date = event.find('date').text
        data.append({'country_txt': country, 'date': date})

    # Convert to DataFrame
    terrorism_df = pd.DataFrame(data)

    # Apply the safe_parse_date function to the 'date' column
    terrorism_df['date'] = terrorism_df['date'].apply(safe_parse_date)
    terrorism_df = terrorism_df.dropna(subset=['date'])

    # Filter data for attacks in the United States
    us_attacks_df = terrorism_df[terrorism_df['country_txt'] == 'United States']

    # Count attacks per year
    attack_count = us_attacks_df.groupby(us_attacks_df['date'].dt.year).size().reset_index(name='attack_count')

    # Load and process data from the JSON file
    json_file = './DATA/commodity_prices_filtered.json'
    with open(json_file, 'r') as f:
        commodity_prices = json.load(f)

    # Create DataFrame from commodity prices data
    commodity_df = pd.DataFrame(commodity_prices)
    commodity_df['date'] = pd.to_datetime(commodity_df['date'])

    # Filter oil prices and group by year
    oil_df = commodity_df[['date', 'oil_dubai']]
    oil_df['year'] = oil_df['date'].dt.year
    oil_df = oil_df.groupby('year').mean().reset_index()

    # Merge datasets on the basis of year
    attack_count.rename(columns={'date': 'year'}, inplace=True)
    merged_df = pd.merge(oil_df, attack_count, on='year', how='left')
    merged_df['attack_count'] = merged_df['attack_count'].fillna(0)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(15, 7))

    color = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Price of oil_dubai', color=color)
    ax1.plot(merged_df['year'], merged_df['oil_dubai'], color=color, label='Price of oil_dubai')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Number of Attacks', color=color)
    ax2.plot(merged_df['year'], merged_df['attack_count'], color=color, label='Number of Attacks')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Relationship between the price of oil_dubai and the number of attacks in the United States')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    # Return the Figure object
    return fig



