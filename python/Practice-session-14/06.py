# Create a Point class to represent a point in 2D space with attribute x and y. Use a constructor to initialize these and a method to calculate the distance between two points
import math

class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def dis_bet_two_points(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        print(f"{distance}")

ob1 = Point(3, 7, 4, 1)
ob1.dis_bet_two_points()
