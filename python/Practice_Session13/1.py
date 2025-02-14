# 1.Create a class Person with a constructor that initializes name and age. Print the details of an object.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name is {self.name} and the age is {self.age}")

obj = Person("Aman",23)
obj.display()
