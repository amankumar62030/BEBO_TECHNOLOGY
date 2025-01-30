# Create a Person class with a constructor that accepts name and age as parameter. Add a method to display this information. Test the constructor by creating objects with different values.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name:{self.name} and Age:{self.age}")

ob1 = Person("David",22)
ob1.display()

ob2 = Person("ROy",21)
ob2.display()