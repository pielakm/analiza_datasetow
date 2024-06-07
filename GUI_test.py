import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Secure coding is not enabled for restorable state")

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from oil_price_into_attacks import create_plot_ropa_terroryzm2

# Create the main window
root = tk.Tk()
root.title("Plot in Tkinter")

# Function to display the plot
def show_plot():
    fig = create_plot_ropa_terroryzm2()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Add a button to trigger the plot display
button = tk.Button(root, text="Show Plot", command=show_plot)
button.pack(pady=10)

# Run the application
root.mainloop()
