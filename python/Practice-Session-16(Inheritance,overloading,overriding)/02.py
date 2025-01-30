# 2. Define a class Shape with a method area that raises a NotimplementedError. Create subclasses
# Rectangle and Circle that implement the area() method.


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r ** 2

rect = Rectangle(5, 10)
print(rect.area())

circle = Circle(7)
print(circle.area())







