# 13.	Create a function that accepts another function and two numbers as arguments and applies the passed function to the numbers.

def func_1(a,b):
    return a+b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

a1 = func_1(a,b)

def func_2(a1,c,d):
    return a1,c,d
c=int(input("Enter the first number:"))
d=int(input("Enter the second number:"))
print(func_2(a1,c,d))
