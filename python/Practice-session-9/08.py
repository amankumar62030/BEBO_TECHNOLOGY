# 8.	Write a program to calculate the area of a rectangle where the default height is 10.

def area_of_rect(l,b=10):
    area = l*b
    return area
l = 20
print(area_of_rect(l))