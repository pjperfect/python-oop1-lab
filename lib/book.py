#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self._page_count += 1

    def get_page(self):
        return self._page_count
    
    def set_page(self, value):
        if type(int) is int and value >= 0:
            self._page_count = value
        else:
            print("page_count must be an integer")

    page_count = property(get_page, set_page)
        