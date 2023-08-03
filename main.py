import os
import sys
import importlib
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme="equilux") 

log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # Adjust this to the path where you want the logs to be saved
sys.stdout = open(os.path.join(log_path, 'stdout.log'), 'w')
sys.stderr = open(os.path.join(log_path, 'stderr.log'), 'w')

WIDGETS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'widgets')  # Absolute path

def load_widget(widget_name):
    print("Loading widget: " + widget_name)
    sys.path.insert(0, WIDGETS_DIR)  # Add WIDGETS_DIR to the module search path
    module = importlib.import_module(f"{widget_name}")
    WidgetClass = getattr(module, 'Widget')
    print("Widget class obtained")
    widget = WidgetClass()  # Remove 'frame' argument
    print("Widget instance created")
    return widget

root = tk.Tk()
root.geometry("800x480")

# Configure the grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Upper left frame
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='nsew')
btc_widget = load_widget('btc_price', frame1).get_tk_object()
btc_widget.grid(sticky='nsew')

# Upper right frame
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky='nsew')
tk.Label(frame2, text="Widget 2").grid(sticky='nsew')

# Lower left frame
frame3 = tk.Frame(root)
frame3.grid(row=1, column=0, sticky='nsew')
tk.Label(frame3, text="Widget 3").grid(sticky='nsew')

# Lower right frame
frame4 = tk.Frame(root)
frame4.grid(row=1, column=1, sticky='nsew')
tk.Label(frame4, text="Widget 4").grid(sticky='nsew')

root.mainloop()
