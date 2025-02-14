# 11.	Create a class Library to add, borrow, and display books.

class Library:
    def __init__(self):
        self.books = []  # List to store available books

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added to the library.')

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You borrowed "{book}".')
        else:
            print(f'"{book}" is not available.')

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:", self.books)

# Example Usage:
library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures")
library.display_books()
library.borrow_book("Python Programming")
library.display_books()
