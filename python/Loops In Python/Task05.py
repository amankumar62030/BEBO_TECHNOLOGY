# Count the number of digits

n = int(input("Enter the number: "))

i = 1
count = 0
while(i <= n):
    n = n%10
    count+=n
    n = n/10
print(count)
