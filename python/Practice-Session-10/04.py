# 4.	Write a function to calculate the area of a rectangle, given its length and breadth.


def area(l,b):
    a = l*b
    return a
l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))
print(area(l,b))