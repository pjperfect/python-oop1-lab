#!/usr/bin/env python3

class Coffee:
    pass
    def __init__(self, size, price):
        self._size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

    def get_size(self):
        return self._size
    
    def set_size(self, value):
        value = value.lower()
        if value in ["small", "medium", "large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    size = property(get_size, set_size)