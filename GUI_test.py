import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from attacks_by_region import attacks_by_region
from count_attacks_world import count_attacks_world
from oil_brent_min_max_price import oil_brent_min_max_price
from oil_brent_to_attacksUSA import oil_brent_to_attacksUSA

# Funkcje generujące wykresy
def generate_attacks_by_region():
    plots["AttacksByRegion"] = attacks_by_region()

def generate_count_attacks_world():
    plots["CountAttacksWorld"] = count_attacks_world()

def generate_oil_brent_min_max_price():
    plots["OilBrentMinMaxPrice"] = oil_brent_min_max_price()

def generate_oil_brent_to_attack():
    plots["OilBrentToAttacksUSA"] = oil_brent_to_attacksUSA()

# Funkcja wyświetlająca wykresy po prawej stronie
def show_plot(fig):
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()  # Usunięcie poprzedniego wykresu

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Funkcje wyświetlające wykresy dla przycisków
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

def show_oil_brent_to_attack():
    if "OilBrentToAttacksUSA" not in plots:
        generate_oil_brent_to_attack()
    show_plot(plots["OilBrentToAttacksUSA"])

# Utworzenie głównego okna
root = tk.Tk()
root.title("Wyświetlanie wykresów")

# Utworzenie ramki po lewej stronie dla przycisków
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Utworzenie przycisków
button1 = ttk.Button(button_frame, text="Ataki według regionu", command=show_attacks_by_region)
button1.pack(fill=tk.X, padx=10, pady=5)

button2 = ttk.Button(button_frame, text="Liczba ataków na świecie", command=show_count_attacks_world)
button2.pack(fill=tk.X, padx=10, pady=5)

button3 = ttk.Button(button_frame, text="Cena ropy Brent", command=show_oil_brent_min_max_price)
button3.pack(fill=tk.X, padx=10, pady=5)

button4 = ttk.Button(button_frame, text="Związek ceny ropy Brent z atakami w USA", command=show_oil_brent_to_attack)
button4.pack(fill=tk.X, padx=10, pady=5)

# Utworzenie ramki po prawej stronie dla wykresów
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Zmienna globalna przechowująca wykresy
plots = {}

# Zmienna globalna przechowująca wykresy
canvas = None

# Uruchomienie pętli głównej
root.mainloop()
