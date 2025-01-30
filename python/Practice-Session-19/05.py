# Write a program that accepts a number from the user and calculates its square root.
# Raise a ValueError if the input is negative, and handle it gracefully.
import math
def square_root(n):
    print(math.sqrt(n))
try:

    n = int(input("Enter the number: "))
    if n>0:
        square_root(n)
    else:
        raise ValueError("The input is negative")

except ValueError as e:
    print(e)