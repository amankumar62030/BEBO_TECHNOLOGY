# 5.	Create a class Car with:
# •	An instance variable brand
# •	A class variable wheels initialized to 4
# •	Add a method show() to print both variables.


class Car:
    wheels = 4

    def __init__(self,brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}, Wheels = {self.wheels}")

car1 = Car("Toyota")
car1.show()
car2 = Car("Tata")
car2.show()