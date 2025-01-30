# 2.	Create a class Animal with an __init__ method that initializes the name of the animal. Create a
# child class Dog that calls the parent’s __init__ method using super() and adds an additional attribute,
# breed.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

dog = Dog("Buddy", "Golden Retriever")
dog.display_info()
