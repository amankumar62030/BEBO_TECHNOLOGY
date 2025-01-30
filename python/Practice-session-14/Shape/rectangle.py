import math
class Rectangle:
    def rect(self,radius):
        self.radius = radius
    def display(self):
        print(f"Area of rectangle is: {2 * math.pi*self.radius}")
