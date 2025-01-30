# 8.	Write a recursive function to find the nth Fibonacci number

n = int(input("Enter the number:"))
first = 0
second = 1
for i in range(n+1):
    temp = first%second
    first=second
    second=temp
print(first)