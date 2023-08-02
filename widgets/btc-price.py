import requests
import tkinter as tk
from PIL import Image, ImageTk
import time
import json
import os

class Widget:  # Change the class name to "Widget"
    def __init__(self):
        self.root = tk.Frame()
        self.label = tk.Label(self.root, text='')
        self.label.pack()
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        self.current_price = None
        self.load_old_price()
        self.update_price()

    def get_tk_object(self):
        return self.root

    def get_btc_price(self):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        return response.json()['bitcoin']['usd']

    def load_old_price(self):
        if os.path.exists('old_price.json'):
            with open('old_price.json', 'r') as f:
                data = json.load(f)
                self.old_price = data['price']
                self.old_price_time = data['time']
        else:
            self.old_price = None
            self.old_price_time = None

    def save_old_price(self):
        with open('old_price.json', 'w') as f:
            json.dump({'price': self.current_price, 'time': time.time()}, f)

    def update_price(self):
        new_price = self.get_btc_price()
        self.label.config(text=f'Bitcoin Price: ${new_price}')

        if self.old_price is not None:
            if new_price > self.old_price:
                # Display green up arrow
                image = Image.open("green_up_arrow.png")
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo  # Keep a reference to the image to prevent garbage collection
            elif new_price < self.old_price:
                # Display red down arrow
                image = Image.open("red_down_arrow.png")
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo  # Keep a reference to the image to prevent garbage collection

        self.current_price = new_price

        if self.old_price is None or time.time() - self.old_price_time > 12 * 60 * 60:
            # 12 hours have passed since the old price was saved
            self.old_price = self.current_price
            self.old_price_time = time.time()
            self.save_old_price()

        self.root.after(60000, self.update_price)  # Update every 60 seconds
