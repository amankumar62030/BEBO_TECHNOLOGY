# 2.	Create a class Book that overrides the __str__ method to display book details.

class Book:
    def __init__(self,title,author,name):
        self.title = title
        self.author = author
        self.name = name

    def __str__(self):
        return f"Title is {self.title} and author is {self.author} and name is {self.name}"

ob = Book("ABC","XUZ","WQE")
print(ob)