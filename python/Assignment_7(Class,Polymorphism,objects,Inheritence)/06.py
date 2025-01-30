# 6.	Create a class Vehicle with attributes name and max_speed. Create a child class Car that adds an
# attribute num_doors. Write a script to create a Car object and display all its attributes.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def show(self):
        print(f"Name: {self.name}, Max Speed: {self.max_speed} km/h")

class Car(Vehicle):
    def __init__(self, name, max_speed, num_doors):
        super().__init__(name, max_speed)
        self.num_doors = num_doors

    def show(self):
        super().show()
        print(f"Number of Doors: {self.num_doors}")

car1 = Car("Toyota", 180, 4)
car2 = Car("Tata", 160, 4)

car1.show()
car2.show()
