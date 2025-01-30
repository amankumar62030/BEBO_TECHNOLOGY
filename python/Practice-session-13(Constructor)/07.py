# Create a class Rectangle with a method to calculate and return the ara

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def display_result(self):
        print(f"Area of rectangle is: {self.l*self.b}")

obj = Rectangle(10,20)
obj.display_result()