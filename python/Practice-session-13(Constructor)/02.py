# Create a class Book that overrides the __str__method to display book details

class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"name: {self.name}, author: {self.author}"
obj = Book("ABC","ABC123")
print(obj)
