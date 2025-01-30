# Create a base class Shape with a method area. Derive classes Rectangle and Circle from Shape and implement the area method for each.


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(f"Area of rectangle: {self.l*self.b}")
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print(f"Area of circle: {3.14*self.r**2}")

ob1 = Rectangle(3,4)
ob1.area()

ob2 = Circle(4)
ob2.area()