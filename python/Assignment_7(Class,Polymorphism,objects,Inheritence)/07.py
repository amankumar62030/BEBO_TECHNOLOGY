# 7.	Use the abc module to create an abstract class Shape with a method area(). Implement this
# class in child classes Square and Circle. Write a script to compute and display the areas of a square
# and a circle using the same method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

square = Square(4)
circle = Circle(3)

print(f"Area of the square: {square.area()}")
print(f"Area of the circle: {circle.area()}")
