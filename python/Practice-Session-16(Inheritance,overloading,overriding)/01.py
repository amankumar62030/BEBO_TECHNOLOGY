# 1. Create a parent class Vehicle with attributes like brand and model. Implement a subclass Car that
# adds an attribute num_doors. Write methods to display the details of both parent and child classes.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_details(self):
        super().display_details()
        print(f"Number of Doors: {self.num_doors}")

car1 = Car("Toyota", "Camry", 4)

car1.display_details()

