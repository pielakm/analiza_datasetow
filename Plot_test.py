from attacks_by_region import attacks_by_region
from count_attacks_world import count_attacks_world
from oil_brent_min_max_price import oil_brent_min_max_price
from oil_brent_to_attacksUSA import oil_brent_to_attacksUSA
from oil_dubai_price import oil_dubai_price
from oil_dubai_to_attacksUSA import oil_dubai_to_attacksUSA
from oil_price_to_attacksUSA import oil_price_to_attacksUSA
from sugar_eu_us_price import sugar_eu_us_price
from sugar_eu_us_world_price import sugar_eu_us_world_price
from sugar_us_to_attacksUS import sugar_us_to_attacksUS
from coffee_arabica_price import coffee_arabica_price
from coffee_robustas_price import coffee_robustas_price
import time

# Functions to generate plots
def generate_plot(function, plot_name):
    start_time = time.time()
    plot = function()
    end_time = time.time()
    print(f"Time taken to generate {plot_name}: {end_time - start_time} seconds")
    return plot

# Functions to display plots
def show_plot(plot):
    # Placeholder for showing the plot in console
    pass

# Function to display plots for buttons
def show_plot_wrapper(generate_function, plot_name):
    generate_plot(generate_function, plot_name)

# Functions to generate plots
functions = [
    ("Attacks by Region", attacks_by_region),
    ("World Attack Count", count_attacks_world),
    ("Brent Oil Price", oil_brent_min_max_price),
    ("Brent Oil Price vs. Attacks in USA", oil_brent_to_attacksUSA),
    ("Dubai Oil Price", oil_dubai_price),
    ("Dubai Oil Price vs. Attacks in USA", oil_dubai_to_attacksUSA),
    ("Oil Prices vs. Attacks in USA", oil_price_to_attacksUSA),
    ("EU and US Sugar Prices", sugar_eu_us_price),
    ("EU, US, and World Sugar Prices", sugar_eu_us_world_price),
    ("Arabica Coffee Prices", coffee_arabica_price),
    ("Robusta Coffee Prices", coffee_robustas_price),
]

for text, function in functions:
    print(f"Generating plot: {text}")
    show_plot_wrapper(function, text)
    print()

