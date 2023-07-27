import sys
import importlib
import tkinter as tk
from tkinter import simpledialog, Toplevel, Listbox

sys.path.append("widgets")  # Add the "widgets" directory to the Python module search path

# A list of available widget names
# You would replace this with a list of your actual widgets
available_widgets = ['Widget1', 'Widget2', 'Widget3', 'Widget4']

def load_widget(module_name, class_name):
    module = importlib.import_module(f"widgets.{module_name}")  # Prefix the module name with "widgets."
    WidgetClass = getattr(module, class_name)
    widget = WidgetClass()
    return widget

def choose_widget(button):
    def on_select(evt):
        # Note here that Tkinter passes an event object to on_select()
        w = evt.widget
        index = int(w.curselection()[0])
        widget_name = w.get(index)
        # Replace the old widget with the new one
        # You would replace "module" with the actual module name for the chosen widget
        new_widget = load_widget(widget_name, "WidgetClass").get_tk_object()  # Assume the widget class name is "WidgetClass"
        button.grid_forget()  # Remove the old button
        new_widget.grid(row=button.grid_info()['row'], column=button.grid_info()['column'])  # Add the new widget
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
