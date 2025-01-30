# Write a function called sum_of_digits that takes an integer and returns the sum of its digits. Use arithmetic operators to extract the digits

n = int(input("Enter the number: "))
sum = 0

for i in range(1,n+1):
    rem = n%10
    sum+=rem
    n//=10
print(sum)