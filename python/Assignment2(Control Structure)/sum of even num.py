# Sum of Even Numbers: Create a program that accepts a positive integer n and calculates the sum of all even numbers from 1 to n. For example, if n is 10, the output should be 30 (2 + 4 + 6 + 8 + 10).

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i
print(sum)
