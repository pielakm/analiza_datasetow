# # # import tkinter as tk
# # # from tkinter import ttk
# # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # from attacks_by_region import attacks_by_region
# # # from count_attacks_world import count_attacks_world
# # # from oil_brent_min_max_price import oil_brent_min_max_price
# # # from oil_brent_to_attacksUSA import oil_brent_to_attacksUSA
# # # from oil_dubai_price import oil_dubai_price
# # # from oil_dubai_to_attacksUSA import oil_dubai_to_attacks
# # # from oil_price_to_attacksUSA import oil_price_to_attacks
# # # from sugar_eu_us_price import sugar_eu_us_price
# # # from sugar_eu_us_world_price import sugar_eu_us_world_price
# # # from sugar_us_to_attacksUS import sugar_us_to_attacksUS
# # # from coffee_arabica_price import coffee_arabica_price
# # # from coffee_robustas_price import coffee_robustas_price
#
# # # # Funkcje generujące wykresy
# # # def generate_attacks_by_region():
# # #     plots["AttacksByRegion"] = attacks_by_region()
#
# # # def generate_count_attacks_world():
# # #     plots["CountAttacksWorld"] = count_attacks_world()
#
# # # def generate_oil_brent_min_max_price():
# # #     plots["OilBrentMinMaxPrice"] = oil_brent_min_max_price()
#
# # # def generate_oil_brent_to_attack():
# # #     plots["OilBrentToAttacksUSA"] = oil_brent_to_attacksUSA()
#
# # # def generate_oil_dubai_price():
# # #     plots["OilDubaiPrice"] = oil_dubai_price()
#
# # # def generate_oil_dubai_to_attacks():
# # #     plots["OilDubaiToAttacksUSA"] = oil_dubai_to_attacks()
#
# # # def generate_oil_price_to_attacks():
# # #     plots["OilPriceToAttacksUSA"] = oil_price_to_attacks()
#
# # # def generate_sugar_eu_us_price():
# # #     plots["SugarEuUsPrice"] = sugar_eu_us_price()
#
# # # def generate_sugar_us_to_attacksUS():
# # #     plots["SugarUsPriceToAttacksUSA"] = sugar_us_to_attacksUS()
#
# # # def generate_sugar_eu_us_world_price():
# # #     plots["SugarEuUsWorldPrice"] = sugar_eu_us_world_price()
#
# # # def generate_coffee_arabica_prices():
# # #     plots["CoffeePriceArabica"] = coffee_arabica_price()
#
# # # def generate_coffee_robustas_prices():
# # #     plots["CoffeePriceRobustas"] = coffee_robustas_price()
#
# # # # Funkcja wyświetlająca wykresy po prawej stronie
# # # def show_plot(fig):
# # #     global canvas
# # #     if canvas is not None:
# # #         canvas.get_tk_widget().destroy()  # Usunięcie poprzedniego wykresu
#
# # #     canvas = FigureCanvasTkAgg(fig, master=plot_frame)
# # #     canvas.draw()
# # #     canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# # # # Funkcje wyświetlające wykresy dla przycisków
# # # def show_attacks_by_region():
# # #     if "AttacksByRegion" not in plots:
# # #         generate_attacks_by_region()
# # #     show_plot(plots["AttacksByRegion"])
#
# # # def show_count_attacks_world():
# # #     if "CountAttacksWorld" not in plots:
# # #         generate_count_attacks_world()
# # #     show_plot(plots["CountAttacksWorld"])
#
# # # def show_oil_brent_min_max_price():
# # #     if "OilBrentMinMaxPrice" not in plots:
# # #         generate_oil_brent_min_max_price()
# # #     show_plot(plots["OilBrentMinMaxPrice"])
#
# # # def show_oil_brent_to_attack():
# # #     if "OilBrentToAttacksUSA" not in plots:
# # #         generate_oil_brent_to_attack()
# # #     show_plot(plots["OilBrentToAttacksUSA"])
#
# # # def show_oil_dubai_price():
# # #     if "OilDubaiPrice" not in plots:
# # #         generate_oil_dubai_price()
# # #     show_plot(plots["OilDubaiPrice"])
#
# # # def show_oil_dubai_to_attacks():
# # #     if "OilDubaiToAttacksUSA" not in plots:
# # #         generate_oil_dubai_to_attacks()
# # #     show_plot(plots["OilDubaiToAttacksUSA"])
#
# # # def show_oil_price_to_attacks():
# # #     if "OilPriceToAttacksUSA" not in plots:
# # #         generate_oil_price_to_attacks()
# # #     show_plot(plots["OilPriceToAttacksUSA"])
#
# # # def show_sugar_eu_us_price():
# # #     if "SugarEuUsPrice" not in plots:
# # #         generate_sugar_eu_us_price()
# # #     show_plot(plots["SugarEuUsPrice"])
#
# # # def show_sugar_us_price():
# # #     if "SugarUsPriceToAttacksUSA" not in plots:
# # #         generate_sugar_eu_us_price()
# # #     show_plot(plots["SugarUsPriceToAttacksUSA"])
#
# # # def show_sugar_eu_us_world_price():
# # #     if "SugarEuUsWorldPrice" not in plots:
# # #         generate_sugar_eu_us_price()
# # #     show_plot(plots["SugarEuUsWorldPrice"])
#
# # # def show_coffee_arabica_prices():
# # #     if "CoffeePriceArabica" not in plots:
# # #         generate_coffee_arabica_prices()
# # #     show_plot(plots["CoffeePriceArabica"])
#
# # # def show_coffee_robustas_prices():
# # #     if "CoffeePriceRobustas" not in plots:
# # #         generate_coffee_robustas_prices()
# # #     show_plot(plots["CoffeePriceRobustas"])
#
# # # # Utworzenie głównego okna
# # # root = tk.Tk()
# # # root.title("Wyświetlanie wykresów")
#
# # # # Utworzenie ramki po lewej stronie dla przycisków
# # # button_frame = ttk.Frame(root)
# # # button_frame.pack(side=tk.LEFT, fill=tk.Y)
#
# # # # Utworzenie przycisków
# # # button1 = ttk.Button(button_frame, text="Ataki według regionu", command=show_attacks_by_region)
# # # button1.pack(fill=tk.X, padx=10, pady=5)
#
# # # button2 = ttk.Button(button_frame, text="Liczba ataków na świecie", command=show_count_attacks_world)
# # # button2.pack(fill=tk.X, padx=10, pady=5)
#
# # # button3 = ttk.Button(button_frame, text="Cena ropy Brent", command=show_oil_brent_min_max_price)
# # # button3.pack(fill=tk.X, padx=10, pady=5)
#
# # # button4 = ttk.Button(button_frame, text="Związek ceny ropy Brent z atakami w USA", command=show_oil_brent_to_attack)
# # # button4.pack(fill=tk.X, padx=10, pady=5)
#
# # # button5 = ttk.Button(button_frame, text="Cena ropy Dubai", command=show_oil_dubai_price)
# # # button4.pack(fill=tk.X, padx=10, pady=5)
#
# # # button6 = ttk.Button(button_frame, text="Związek ceny ropy Dubai z atakami w USA", command=show_oil_dubai_price)
# # # button6.pack(fill=tk.X, padx=10, pady=5)
#
# # # button7 = ttk.Button(button_frame, text="Związek ceny ropy Dubai oraz Brent z atakami w USA", command=show_oil_price_to_attacks)
# # # button7.pack(fill=tk.X, padx=10, pady=5)
#
# # # button8 = ttk.Button(button_frame, text="Związek ceny cukru europejskiego a cukru amerykańskiego", command=show_sugar_eu_us_price)
# # # button8.pack(fill=tk.X, padx=10, pady=5)
#
# # # button9 = ttk.Button(button_frame, text="Związek ceny cukru europejskiego, cukru amerykańskiego do ceny światowej cukru", command=show_sugar_eu_us_world_price)
# # # button9.pack(fill=tk.X, padx=10, pady=5)
#
# # # button10 = ttk.Button(button_frame, text="Ceny kawy arabiki", command=show_coffee_arabica_prices)
# # # button10.pack(fill=tk.X, padx=10, pady=5)
#
# # # button11 = ttk.Button(button_frame, text="Ceny kawy robusty", command=show_coffee_robustas_prices)
# # # button11.pack(fill=tk.X, padx=10, pady=5)
#
# # # # Utworzenie ramki po prawej stronie dla wykresów
# # # plot_frame = ttk.Frame(root)
# # # plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # # # Zmienna globalna przechowująca wykresy
# # # plots = {}
#
# # # # Zmienna globalna przechowująca wykresy
# # # canvas = None
#
# # # # Uruchomienie pętli głównej
# # # root.mainloop()
#
# # import tkinter as tk
# # from tkinter import ttk
# # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # from attacks_by_region import attacks_by_region
# # from count_attacks_world import count_attacks_world
# # from oil_brent_min_max_price import oil_brent_min_max_price
# # from oil_brent_to_attacksUSA import oil_brent_to_attacksUSA
# # from oil_dubai_price import oil_dubai_price
# # from oil_dubai_to_attacksUSA import oil_dubai_to_attacksUSA  # Corrected import name
# # from oil_price_to_attacksUSA import oil_price_to_attacksUSA  # Corrected import name
# # from sugar_eu_us_price import sugar_eu_us_price
# # from sugar_eu_us_world_price import sugar_eu_us_world_price
# # from sugar_us_to_attacksUS import sugar_us_to_attacksUS
# # from coffee_arabica_price import coffee_arabica_price
# # from coffee_robustas_price import coffee_robustas_price
#
# # # Functions to generate plots
# # def generate_attacks_by_region():
# #     plots["AttacksByRegion"] = attacks_by_region()
#
# # def generate_count_attacks_world():
# #     plots["CountAttacksWorld"] = count_attacks_world()
#
# # def generate_oil_brent_min_max_price():
# #     plots["OilBrentMinMaxPrice"] = oil_brent_min_max_price()
#
# # def generate_oil_brent_to_attacksUSA():
# #     plots["OilBrentToAttacksUSA"] = oil_brent_to_attacksUSA()
#
# # def generate_oil_dubai_price():
# #     plots["OilDubaiPrice"] = oil_dubai_price()
#
# # def generate_oil_dubai_to_attacksUSA():
# #     plots["OilDubaiToAttacksUSA"] = oil_dubai_to_attacksUSA()
#
# # def generate_oil_price_to_attacksUSA():
# #     plots["OilPriceToAttacksUSA"] = oil_price_to_attacksUSA()
#
# # def generate_sugar_eu_us_price():
# #     plots["SugarEuUsPrice"] = sugar_eu_us_price()
#
# # def generate_sugar_us_to_attacksUS():
# #     plots["SugarUsPriceToAttacksUSA"] = sugar_us_to_attacksUS()
#
# # def generate_sugar_eu_us_world_price():
# #     plots["SugarEuUsWorldPrice"] = sugar_eu_us_world_price()
#
# # def generate_coffee_arabica_price():
# #     plots["CoffeePriceArabica"] = coffee_arabica_price()
#
# # def generate_coffee_robustas_price():
# #     plots["CoffeePriceRobustas"] = coffee_robustas_price()
#
# # # Function to show the plots
# # def show_plot(fig):
# #     global canvas
# #     if canvas is not None:
# #         canvas.get_tk_widget().destroy()  # Remove the previous plot
#
# #     canvas = FigureCanvasTkAgg(fig, master=plot_frame)
# #     canvas.draw()
# #     canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# # # Functions to display plots for buttons
# # def show_attacks_by_region():
# #     if "AttacksByRegion" not in plots:
# #         generate_attacks_by_region()
# #     show_plot(plots["AttacksByRegion"])
#
# # def show_count_attacks_world():
# #     if "CountAttacksWorld" not in plots:
# #         generate_count_attacks_world()
# #     show_plot(plots["CountAttacksWorld"])
#
# # def show_oil_brent_min_max_price():
# #     if "OilBrentMinMaxPrice" not in plots:
# #         generate_oil_brent_min_max_price()
# #     show_plot(plots["OilBrentMinMaxPrice"])
#
# # def show_oil_brent_to_attacksUSA():
# #     if "OilBrentToAttacksUSA" not in plots:
# #         generate_oil_brent_to_attacksUSA()
# #     show_plot(plots["OilBrentToAttacksUSA"])
#
# # def show_oil_dubai_price():
# #     if "OilDubaiPrice" not in plots:
# #         generate_oil_dubai_price()
# #     show_plot(plots["OilDubaiPrice"])
#
# # def show_oil_dubai_to_attacksUSA():
# #     if "OilDubaiToAttacksUSA" not in plots:
# #         generate_oil_dubai_to_attacksUSA()
# #     show_plot(plots["OilDubaiToAttacksUSA"])
#
# # def show_oil_price_to_attacksUSA():
# #     if "OilPriceToAttacksUSA" not in plots:
# #         generate_oil_price_to_attacksUSA()
# #     show_plot(plots["OilPriceToAttacksUSA"])
#
# # def show_sugar_eu_us_price():
# #     if "SugarEuUsPrice" not in plots:
# #         generate_sugar_eu_us_price()
# #     show_plot(plots["SugarEuUsPrice"])
#
# # def show_sugar_us_to_attacksUS():
# #     if "SugarUsPriceToAttacksUSA" not in plots:
# #         generate_sugar_us_to_attacksUS()
# #     show_plot(plots["SugarUsPriceToAttacksUSA"])
#
# # def show_sugar_eu_us_world_price():
# #     if "SugarEuUsWorldPrice" not in plots:
# #         generate_sugar_eu_us_world_price()
# #     show_plot(plots["SugarEuUsWorldPrice"])
#
# # def show_coffee_arabica_price():
# #     if "CoffeePriceArabica" not in plots:
# #         generate_coffee_arabica_price()
# #     show_plot(plots["CoffeePriceArabica"])
#
# # def show_coffee_robustas_price():
# #     if "CoffeePriceRobustas" not in plots:
# #         generate_coffee_robustas_price()
# #     show_plot(plots["CoffeePriceRobustas"])
#
# # # Create main window
# # root = tk.Tk()
# # root.title("Plot Display")
#
# # # Create frame on the left for buttons
# # button_frame = ttk.Frame(root)
# # button_frame.pack(side=tk.LEFT, fill=tk.Y)
#
# # # Create buttons
# # buttons = [
# #     ("Attacks by Region", show_attacks_by_region),
# #     ("World Attack Count", show_count_attacks_world),
# #     ("Brent Oil Price", show_oil_brent_min_max_price),
# #     ("Brent Oil Price vs. Attacks in USA", show_oil_brent_to_attacksUSA),
# #     ("Dubai Oil Price", show_oil_dubai_price),
# #     ("Dubai Oil Price vs. Attacks in USA", show_oil_dubai_to_attacksUSA),
# #     ("Oil Prices vs. Attacks in USA", show_oil_price_to_attacksUSA),
# #     ("EU and US Sugar Prices", show_sugar_eu_us_price),
# #     ("EU, US, and World Sugar Prices", show_sugar_eu_us_world_price),
# #     ("Arabica Coffee Prices", show_coffee_arabica_price),
# #     ("Robusta Coffee Prices", show_coffee_robustas_price),
# # ]
#
# # for text, command in buttons:
# #     button = ttk.Button(button_frame, text=text, command=command)
# #     button.pack(fill=tk.X, padx=10, pady=5)
#
# # # Create frame on the right for plots
# # plot_frame = ttk.Frame(root)
# # plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # # Global variable to store plots
# # plots = {}
#
# # # Global variable to store the canvas
# # canvas = None
#
# # # Run the main loop
# # root.mainloop()
#
#
import tkinter as tk
from tkinter import ttk
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
    ("Brent Oil Price vs. Attacks in USA", show_oil_brent_to_attacksUSA),
    ("Dubai Oil Price", show_oil_dubai_price),
    ("Dubai Oil Price vs. Attacks in USA", show_oil_dubai_to_attacksUSA),
    ("Oil Prices vs. Attacks in USA", show_oil_price_to_attacksUSA),
    ("EU and US Sugar Prices", show_sugar_eu_us_price),
    ("EU, US, and World Sugar Prices", show_sugar_eu_us_world_price),
    ("Arabica Coffee Prices", show_coffee_arabica_price),
    ("Robusta Coffee Prices", show_coffee_robustas_price),
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


#
# import tkinter as tk
# from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from attacks_by_region import attacks_by_region
# from count_attacks_world import count_attacks_world
# from oil_brent_min_max_price import oil_brent_min_max_price
# from oil_brent_to_attacksUSA import oil_brent_to_attacksUSA
#
# # Funkcje generujące wykresy
# def generate_attacks_by_region():
#     plots["AttacksByRegion"] = attacks_by_region()
#
# def generate_count_attacks_world():
#     plots["CountAttacksWorld"] = count_attacks_world()
#
# def generate_oil_brent_min_max_price():
#     plots["OilBrentMinMaxPrice"] = oil_brent_min_max_price()
#
# def generate_oil_brent_to_attack():
#     plots["OilBrentToAttacksUSA"] = oil_brent_to_attacksUSA()
#
# # Funkcja wyświetlająca wykresy po prawej stronie
# def show_plot(fig):
#     global canvas
#     if canvas is not None:
#         canvas.get_tk_widget().destroy()  # Usunięcie poprzedniego wykresu
#
#     canvas = FigureCanvasTkAgg(fig, master=plot_frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# # Funkcje wyświetlające wykresy dla przycisków
# def show_attacks_by_region():
#     if "AttacksByRegion" not in plots:
#         generate_attacks_by_region()
#     show_plot(plots["AttacksByRegion"])
#
# def show_count_attacks_world():
#     if "CountAttacksWorld" not in plots:
#         generate_count_attacks_world()
#     show_plot(plots["CountAttacksWorld"])
#
# def show_oil_brent_min_max_price():
#     if "OilBrentMinMaxPrice" not in plots:
#         generate_oil_brent_min_max_price()
#     show_plot(plots["OilBrentMinMaxPrice"])
#
# def show_oil_brent_to_attack():
#     if "OilBrentToAttacksUSA" not in plots:
#         generate_oil_brent_to_attack()
#     show_plot(plots["OilBrentToAttacksUSA"])
#
# # Utworzenie głównego okna
# root = tk.Tk()
# root.title("Wyświetlanie wykresów")
#
# # Utworzenie ramki po lewej stronie dla przycisków
# button_frame = ttk.Frame(root)
# button_frame.pack(side=tk.LEFT, fill=tk.Y)
#
# # Utworzenie przycisków
# button1 = ttk.Button(button_frame, text="Ataki według regionu", command=show_attacks_by_region)
# button1.pack(fill=tk.X, padx=10, pady=5)
#
# button2 = ttk.Button(button_frame, text="Liczba ataków na świecie", command=show_count_attacks_world)
# button2.pack(fill=tk.X, padx=10, pady=5)
#
# button3 = ttk.Button(button_frame, text="Cena ropy Brent", command=show_oil_brent_min_max_price)
# button3.pack(fill=tk.X, padx=10, pady=5)
#
# button4 = ttk.Button(button_frame, text="Związek ceny ropy Brent z atakami w USA", command=show_oil_brent_to_attack)
# button4.pack(fill=tk.X, padx=10, pady=5)
#
# # Utworzenie ramki po prawej stronie dla wykresów
# plot_frame = ttk.Frame(root)
# plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # Zmienna globalna przechowująca wykresy
# plots = {}
#
# # Zmienna globalna przechowująca wykresy
# canvas = None
#
# # Uruchomienie pętli głównej
# root.mainloop()