
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
import requests
JWT_TOKEN = ''
def login():
    response = requests.post('http://localhost:5000/login', json={'username': 'root', 'password': ''})
    if(response.json().get('access_token')):
        global JWT_TOKEN
        JWT_TOKEN = response.json().get('access_token')
        messagebox.showinfo("Login", "Logged in successfully!")
        return True
    else:
        messagebox.showinfo("Login", "Not loggined in!")
        return False

def export_to_database():
    if(JWT_TOKEN != ''):
        headers = {
            'Authorization': f'Bearer {JWT_TOKEN}'
        }
        response = requests.post('http://localhost:5000/load_from_xml', headers=headers)
        count = requests.get('http://localhost:5000/count_events', headers=headers)
        messagebox.showinfo("Export to Database", f"Data exported to database successfully! Counted data: {count.json().get('count')}")
        return True
    else:
        messagebox.showinfo("Login", "Not loggined in!")
        return False
def export_to_csv():
    if(JWT_TOKEN != ''):
        headers = {
            'Authorization': f'Bearer {JWT_TOKEN}'
        }
        response = requests.get('http://localhost:5000/export_to_csv', headers=headers)
        messagebox.showinfo("Export to CSV", "Data exported to CSV successfully!")
    else:
        messagebox.showinfo("Login", "Not loggined in!")
        return False

# Functions to generate plots
def generate_attacks_by_region():
    plots["AttacksByRegion"] = attacks_by_region()

def generate_count_attacks_world():
    plots["CountAttacksWorld"] = count_attacks_world()

def generate_oil_brent_min_max_price():
    plots["OilBrentMinMaxPrice"] = oil_brent_min_max_price()

def generate_oil_brent_to_attacksUSA():
    plots["OilBrentToAttacksUSA"] = oil_brent_to_attacksUSA()

def generate_oil_dubai_price():
    plots["OilDubaiPrice"] = oil_dubai_price()

def generate_oil_dubai_to_attacksUSA():
    plots["OilDubaiToAttacksUSA"] = oil_dubai_to_attacksUSA()

def generate_oil_price_to_attacksUSA():
    plots["OilPriceToAttacksUSA"] = oil_price_to_attacksUSA()

def generate_sugar_eu_us_price():
    plots["SugarEuUsPrice"] = sugar_eu_us_price()

def generate_sugar_us_to_attacksUS():
    plots["SugarUsPriceToAttacksUSA"] = sugar_us_to_attacksUS()

def generate_sugar_eu_us_world_price():
    plots["SugarEuUsWorldPrice"] = sugar_eu_us_world_price()

def generate_coffee_arabica_price():
    plots["CoffeePriceArabica"] = coffee_arabica_price()

def generate_coffee_robustas_price():
    plots["CoffeePriceRobustas"] = coffee_robustas_price()

# Function to show the plots
def show_plot(fig):
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()  # Remove the previous plot

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Functions to display plots for buttons
def show_attacks_by_region():
    if "AttacksByRegion" not in plots:
        generate_attacks_by_region()
    show_plot(plots["AttacksByRegion"])

def show_count_attacks_world():
    if "CountAttacksWorld" not in plots:
        generate_count_attacks_world()
    show_plot(plots["CountAttacksWorld"])

def show_oil_brent_min_max_price():
    if "OilBrentMinMaxPrice" not in plots:
        generate_oil_brent_min_max_price()
    show_plot(plots["OilBrentMinMaxPrice"])

def show_oil_brent_to_attacksUSA():
    if "OilBrentToAttacksUSA" not in plots:
        generate_oil_brent_to_attacksUSA()
    show_plot(plots["OilBrentToAttacksUSA"])

def show_oil_dubai_price():
    if "OilDubaiPrice" not in plots:
        generate_oil_dubai_price()
    show_plot(plots["OilDubaiPrice"])

def show_oil_dubai_to_attacksUSA():
    if "OilDubaiToAttacksUSA" not in plots:
        generate_oil_dubai_to_attacksUSA()
    show_plot(plots["OilDubaiToAttacksUSA"])

def show_oil_price_to_attacksUSA():
    if "OilPriceToAttacksUSA" not in plots:
        generate_oil_price_to_attacksUSA()
    show_plot(plots["OilPriceToAttacksUSA"])

def show_sugar_eu_us_price():
    if "SugarEuUsPrice" not in plots:
        generate_sugar_eu_us_price()
    show_plot(plots["SugarEuUsPrice"])

def show_sugar_us_to_attacksUS():
    if "SugarUsPriceToAttacksUSA" not in plots:
        generate_sugar_us_to_attacksUS()
    show_plot(plots["SugarUsPriceToAttacksUSA"])

def show_sugar_eu_us_world_price():
    if "SugarEuUsWorldPrice" not in plots:
        generate_sugar_eu_us_world_price()
    show_plot(plots["SugarEuUsWorldPrice"])

def show_coffee_arabica_price():
    if "CoffeePriceArabica" not in plots:
        generate_coffee_arabica_price()
    show_plot(plots["CoffeePriceArabica"])

def show_coffee_robustas_price():
    if "CoffeePriceRobustas" not in plots:
        generate_coffee_robustas_price()
    show_plot(plots["CoffeePriceRobustas"])

# Create main window
root = tk.Tk()
root.title("Plot Display")

# Create frame on the left for buttons
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Create buttons
buttons = [
    ("Attacks by Region", show_attacks_by_region),
    ("World Attack Count", show_count_attacks_world),
    ("Brent Oil Price", show_oil_brent_min_max_price),
    ("Dubai Oil Price", show_oil_dubai_price),
    ("EU and US Sugar Prices", show_sugar_eu_us_price),
    ("EU, US, and World Sugar Prices", show_sugar_eu_us_world_price),
    ("Arabica Coffee Prices", show_coffee_arabica_price),
    ("Robusta Coffee Prices", show_coffee_robustas_price),
    ("Brent Oil Price vs. Attacks in USA", show_oil_brent_to_attacksUSA),
    ("Dubai Oil Price vs. Attacks in USA", show_oil_dubai_to_attacksUSA),
    ("Oil Prices vs. Attacks in USA", show_oil_price_to_attacksUSA),
    ("Login", login),
    ("export_to_database", export_to_database),
    ("export_to_csv", export_to_csv),

]

for text, command in buttons:
    button = ttk.Button(button_frame, text=text, command=command)
    button.pack(fill=tk.X, padx=10, pady=5)

# Create frame on the right for plots
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Global variable to store plots
plots = {}

# Global variable to store the canvas
canvas = None

# Run the main loop
root.mainloop()

