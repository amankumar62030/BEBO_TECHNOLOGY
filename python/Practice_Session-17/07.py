# 7. Create a program to show hierarchical inheritance with a base class Vehicle and derived classes Car
# and Bike.


class Vehicle:
    def m1(self):
        pass
class Car(Vehicle):
    def m1(self):
        print("I am Car")
class Bike(Vehicle):
    def m1(self):
        print("I am Bike")

vehicle = Vehicle()
car = Car()
bike = Bike()

vehicle.m1()
car.m1()
bike.m1()

