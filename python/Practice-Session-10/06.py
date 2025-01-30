# 6.	Write a function that takes three parameters and demonstrates the use of default values for some of them.


def func(a,b,c=30):
    return a,b,c
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(func(a,b))