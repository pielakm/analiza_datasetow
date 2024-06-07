import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


def oil_dubai_price():
    # Read the CSV file into a DataFrame
    df = pd.read_csv("./DATA/commodity_prices_filtered.csv", index_col="date", parse_dates=True, encoding='latin-1')

    # Plot oil_dubai prices against dates
    plt.figure(figsize=(15, 5))
    sns.lineplot(data=df["oil_dubai"], label='Data', color='blue')
    plt.title("Dubai Oil Prices")
    plt.ylabel("Price per Barrel (USD)")
    plt.xlabel("Date")

    # Set major ticks format to show every year
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    # Find maximum and minimum values
    max_value = df["oil_dubai"].max()
    min_value = df["oil_dubai"].min()

    # Find dates for maximum and minimum values
    max_date = df["oil_dubai"].idxmax()
    min_date = df["oil_dubai"].idxmin()

    # Mark the maximum and minimum points on the plot
    plt.scatter(max_date, max_value, color='r', s=30, zorder=5, label=f'Maximum: {max_value:.2f} on {max_date.date()}')
    plt.scatter(min_date, min_value, color='g', s=30, zorder=5, label=f'Minimum: {min_value:.2f} on {min_date.date()}')

    # Rotate date labels for better readability
    plt.xticks(rotation=45)

    # Show legend
    plt.legend()
    return plt

