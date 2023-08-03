#!/usr/bin/env python3

import requests
import tkinter as tk
from PIL import Image, ImageTk
import time
import json
import os
from main import choose_widget

class Widget:  
    def __init__(self, frame):
        self.root = frame
        self.label = tk.Label(self.root, text='')
        self.label.grid(sticky='nsew')
        self.image_label = tk.Label(self.root)
        self.image_label.grid(sticky='nsew')
        self.current_price = None
        self.load_old_price()
        self.update_price()

        change_widget_button = tk.Button(self.root, text="Change widget", command=self.change_widget)
        change_widget_button.grid(sticky='nsew')

    def change_widget(self):
        choose_widget(self.root)
    
    def get_tk_object(self):
        return self.root

    def get_btc_price(self):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        return response.json()['bitcoin']['usd']

    def load_old_price(self):
        old_price_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'old_price.json')
        if os.path.exists(old_price_path):
            with open(old_price_path, 'r') as f:
                data = json.load(f)
                self.old_price = data['price']
                self.old_price_time = data['time']
        else:
            self.old_price = None
            self.old_price_time = None

    def save_old_price(self):
        old_price_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'old_price.json')
        with open(old_price_path, 'w') as f:
            json.dump({'price': self.current_price, 'time': time.time()}, f)

    def update_price(self):
        new_price = self.get_btc_price()
        self.label.config(text=f'Bitcoin Price: ${new_price}')

        script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory containing this script

        if self.old_price is not None:
            if new_price > self.old_price:
                # Display green up arrow
                image_path = os.path.join(script_dir, "btc_price", "green_up_arrow.png") 
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo  # Keep a reference to the image to prevent garbage collection
            elif new_price < self.old_price:
                # Display red down arrow
                image_path = os.path.join(script_dir, "btc_price", "red_down_arrow.png")  # Use the correct path to the image
                image = Image.open(image_path)
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
