# 6.	Create a class Shape with a default constructor that initializes type to "Generic"

class Shape:
    def __init__(self,type="Generic"):
        self.type = type

    def display(self):
        print(f"Type is {self.type}")

ob = Shape()
ob.display()
ob1 = Shape("Circle")
ob1.display()