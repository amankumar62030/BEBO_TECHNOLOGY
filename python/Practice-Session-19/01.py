# Write a program to divide two numbers. Handle the case where the divisor is zero using ZeroDivisionError.

def div(a,b):
    print(a/b)
try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    div(a,b)
except ZeroDivisionError as e:
    print(e)