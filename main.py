#!/usr/bin/env python3

import os
import sys
import importlib
import tkinter as tk
from tkinter import simpledialog, Toplevel, Listbox

log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # Adjust this to the path where you want the logs to be saved
sys.stdout = open(os.path.join(log_path, 'stdout.log'), 'w')
sys.stderr = open(os.path.join(log_path, 'stderr.log'), 'w')

WIDGETS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'widgets')  # Absolute path

available_widgets = [f[:-3] for f in os.listdir(WIDGETS_DIR) if f.endswith('.py') and f != '__init__.py']

def load_widget(widget_name):
    print("Loading widget: " + widget_name)
    sys.path.insert(0, WIDGETS_DIR)  # Add WIDGETS_DIR to the module search path
    module = importlib.import_module(f"{widget_name}")
    WidgetClass = getattr(module, 'Widget')
    print("Widget class obtained")
    widget = WidgetClass()
    print("Widget instance created")
    return widget

def choose_widget(frame):
    def on_select(evt):
        if evt is not None:
            w = evt.widget
            index = int(w.curselection()[0])
            widget_name = w.get(index)
        else:
            widget_name = listbox.get(listbox.curselection())
        print(f"Widget selected: {widget_name}")  # Add this line
        try:
            print("About to load widget")  # Point de contrôle
            new_widget = load_widget(widget_name).get_tk_object()
            print("Widget loaded successfully")  # Point de contrôle
            for widget in frame.winfo_children():
                widget.destroy()
            print("Old widget destroyed")  # Point de contrôle
            new_widget.grid(sticky='nsew')
            print("New widget packed")  # Point de contrôle
            top.destroy()
            print("Top destroyed")  # Point de contrôle
        except Exception as e:
            print(f"Error while loading widget: {str(e)}")


    top = Toplevel(root)
    listbox = Listbox(top)
    listbox.bind('<<ListboxSelect>>', on_select)
    for widget_name in available_widgets:
        listbox.insert(tk.END, widget_name)
    listbox.pack()

    confirm_button = tk.Button(top, text="Valider", command=lambda: on_select(None))
    confirm_button.pack()


root = tk.Tk()
root.geometry("800x480")

# Configure the grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

frames = []
for i in range(2):
    for j in range(2):
        frame = tk.Frame(root)
        frame.grid(row=i, column=j, sticky='nsew')  # Modify here
        frames.append(frame)
        button = tk.Button(frame, text="Choose widget", command=lambda frame=frame: choose_widget(frame))
        button.grid(sticky='nsew')  # Modify here

root.mainloop()
