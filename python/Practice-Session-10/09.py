# 9.	Implement a recursive function to calculate the sum of the digits of a given number.

def sum(num):
    for i in range(num+1):
        return num+num+1
num = int(input("Enter the number: "))
print(sum(num))