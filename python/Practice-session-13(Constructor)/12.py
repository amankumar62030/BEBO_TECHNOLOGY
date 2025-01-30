# Create a class Circle with method to calculate area and circumference

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_of_circle(self):
        return math.pi*self.radius*self.radius

    def circumference_of_circle(self):
        return 2*math.pi*self.radius

ob1 = Circle(5)
print("Area:",ob1.area_of_circle())
print("Circumference: ", ob1.circumference_of_circle())