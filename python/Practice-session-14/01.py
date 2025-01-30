# Implement a Car class with attribute like make, model and year. Include a method start_engine() that points a message indicating the engine is starting . create multiple objects to represent different cars.


class Car:
    def __init__(self,make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"engine is starting-Make:{self.make},Model:{self.model},Year:{self.year}")

ob1 = Car("TATA","NEXON",2021)
ob1.start_engine()
ob2 = Car("Toyota","Innova Hycross",2023)
ob2.start_engine()