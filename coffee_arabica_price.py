import pandas as pd
import json
import matplotlib.pyplot as plt

# Load data from the JSON file
json_file = './DATA/commodity_prices_filtered.json'
with open(json_file, 'r') as f:
    commodity_prices = json.load(f)

def coffee_arabica_price():
    # Create a DataFrame from the data
    commodity_df = pd.DataFrame(commodity_prices)
    commodity_df['date'] = pd.to_datetime(commodity_df['date'])

    # Sort the data by date
    commodity_df = commodity_df.sort_values(by='date')

    # Create a Figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting
    ax.plot(commodity_df['date'], commodity_df['coffee_arabica'], marker='o', linestyle='-', color='b')

    # Add title and axis labels
    ax.set_title('Arabica Coffee Price Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Arabica Coffee Price ($ per lb)')

    # Set grid settings
    ax.grid(True)

    # Return the Figure object
    return fig
