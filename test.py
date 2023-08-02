import sys
import os
import importlib

WIDGETS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'widgets')  # Absolute path

def load_widget(widget_name):
    print("Loading widget: " + widget_name)  # Point de contrôle
    sys.path.insert(0, WIDGETS_DIR)  # Add WIDGETS_DIR to the module search path
    module = importlib.import_module(f"{widget_name}")  # Remove "widgets." prefix
    WidgetClass = getattr(module, 'Widget')
    print("Widget class obtained")  # Point de contrôle
    widget = WidgetClass()
    print("Widget instance created")  # Point de contrôle
    return widget

# Test the function
widget = load_widget('btc_price')
