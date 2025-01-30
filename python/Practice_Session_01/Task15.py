# Write a program that takes a number as input and checks if it falls within a specified range. For example, check if the number is between 10 and 50 (inclusive).

n = int(input("Enter the number: "))

if(n>=10 and n<=50):
    print("The number lies between the given range!")
else:
    print("The number does not lies between the given range!")