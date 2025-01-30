# Create a class Person with a constructor that initialize name and age. Print the details of an object.

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"The name is {self.name} and the age is {self.age}")

obj1 = person("Satwinder", 30)
obj1.display_info()