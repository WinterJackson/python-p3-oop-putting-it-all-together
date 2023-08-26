#!/usr/bin/env python3

class Book:
        def __init__ (self,title,page_count):
            self.title=title
            self.page_count=page_count
            
            if isinstance(page_count, int):
                self.page_count = page_count

        @property
        def page_count(self):
            return self._page_count

        @page_count.setter
        def page_count(self, value):
            if isinstance(value, int):
                self._page_count = value
            else:
                print("page_count must be an integer")

        def turn_page(self):
            print("Flipping the page...wow, you read fast!")
            
book = Book("And Then There Were None", 272)
print(f"{book.title}")

# Access attributes
print(f"Title: {book.title}")
print(f"Page Count: {book.page_count}")

# Access methods
book.turn_page()

# Set new page count
book.page_count = 200

# Print updated page count
print(f"Updated Page Count: {book.page_count}")