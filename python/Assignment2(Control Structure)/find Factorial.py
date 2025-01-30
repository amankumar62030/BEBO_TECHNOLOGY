# Find Factorial: Create a function that accepts a positive integer n and calculates the factorial of n using a loop.

n = int(input("Enter the number: "))

fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)