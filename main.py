#!/usr/bin/env python3

import os
import sys
import importlib
import tkinter as tk
from tkinter import simpledialog, Toplevel, Listbox

WIDGETS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'widgets')

available_widgets = [f[:-3] for f in os.listdir(WIDGETS_DIR) if f.endswith('.py') and f != '__init__.py']

def load_widget(widget_name):
    module = importlib.import_module(f"widgets.{widget_name}")
    WidgetClass = getattr(module, 'Widget')
    widget = WidgetClass()
    return widget

def choose_widget(frame):
    def on_select(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        widget_name = w.get(index)
        try:
            new_widget = load_widget(widget_name).get_tk_object()
            for widget in frame.winfo_children():
                widget.destroy()
            new_widget.pack(fill='both', expand=True)  # Modify here
            top.destroy()
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
        button.pack(fill='both', expand=True)  # Modify here

root.mainloop()
