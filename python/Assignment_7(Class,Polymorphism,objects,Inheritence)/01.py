# 1.	Create a polymorphic function calculate_area() that calculates the area of a Circle, Rectangle,
# and Triangle based on the shape object passed to it.

import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.area()

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(4, 3)

print(f"Area of Circle: {calculate_area(circle)}")
print(f"Area of Rectangle: {calculate_area(rectangle)}")
print(f"Area of Triangle: {calculate_area(triangle)}")
