# 8.	Create a class Book with a constructor that initializes the title. Override the del method
# to print a message when the object is deleted. Create and delete a Book object to demonstrate this.

class Book:
    def __init__(self, title):
        self.title = title  # Initialize the title attribute

    def display(self):
        print(f"Title: {self.title}")

    def __del__(self):
        print(f"The book '{self.title}' has been deleted.")


# Demonstration Block 1
ob1 = Book("The Great Gatsby")
ob2 = Book("1984")

ob1.display()
ob2.display()

del ob1
del ob2

