# Count the number of digits

n = int(input("Enter the number: "))
count=0
while n>0:
    n = n//10
    count+=1
print(count)