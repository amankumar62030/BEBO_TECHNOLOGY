# Develop a package Shape with modules circle.py and rectangle.py. Include methods to calculate the area and perimeter of a circle and rectangle. Test the package in a separate script.




import math
class Circle:
    def area(self,radius):
        self.radius = radius
    def display(self):
        print(f"Area of circle is: {math.pi*self.radius*self.radius}")
