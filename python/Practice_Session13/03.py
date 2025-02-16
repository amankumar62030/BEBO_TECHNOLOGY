# 3.	Create a class Car and print a message when an object is deleted.

class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def __del__(self):
        print(f"Car {self.name} and model {self.model} is deleted")
ob = Car("Safari","VXI")

del ob