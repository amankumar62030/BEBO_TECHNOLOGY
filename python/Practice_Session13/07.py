# 7.	Create a class Rectangle with a method to calculate and return the area.

class Rectange:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"The area of rectangle is : {self.length*self.breadth}")

ar = Rectange(10,20)
ar.area()