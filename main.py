import os
import sys
import importlib
import tkinter as tk
from tkinter import simpledialog, Toplevel, Listbox

# Directory where the widgets are stored
WIDGETS_DIR = os.path.join(os.path.dirname(__file__), 'widgets')

# Scan the "widgets" directory for available widgets
available_widgets = [f[:-3] for f in os.listdir(WIDGETS_DIR) if f.endswith('.py') and f != '__init__.py']

def load_widget(widget_name):
    module = importlib.import_module(f"{WIDGETS_DIR}.{widget_name}")  
    WidgetClass = getattr(module, 'Widget')  # Assume the widget class name is "Widget"
    widget = WidgetClass()
    return widget

def choose_widget(button):
    def on_select(evt):
        # Note here that Tkinter passes an event object to on_select()
        w = evt.widget
        index = int(w.curselection()[0])
        widget_name = w.get(index)
        new_widget = load_widget(widget_name)  # Load the selected widget
        new_widget.grid(row=button.grid_info()['row'], column=button.grid_info()['column'])  # Add the new widget
        button.grid_forget()  # Remove the old button
        top.destroy()  # Close the dialog

    top = Toplevel(root)
    listbox = Listbox(top)
    listbox.bind('<<ListboxSelect>>', on_select)
    for widget_name in available_widgets:
        listbox.insert(tk.END, widget_name)
    listbox.pack()

root = tk.Tk()
root.geometry("800x480")  # Adjust this to match your screen's resolution

# Add buttons to layout
top_left_button = tk.Button(root, text="Choose widget", command=lambda: choose_widget(top_left_button))
top_right_button = tk.Button(root, text="Choose widget", command=lambda: choose_widget(top_right_button))
bottom_left_button = tk.Button(root, text="Choose widget", command=lambda: choose_widget(bottom_left_button))
bottom_right_button = tk.Button(root, text="Choose widget", command=lambda: choose_widget(bottom_right_button))

top_left_button.grid(row=0, column=0)
top_right_button.grid(row=0, column=1)
bottom_left_button.grid(row=1, column=0)
bottom_right_button.grid(row=1, column=1)

root.mainloop()
