# 8.Write a Python function that counts the occurrences of a specific element in a tuple

tup = tuple(map(int,input("Enter the number separated by commas: ").split(",")))
target = int(input("Enter the number: "))

count = 0

for i in tup:
    if i==target:
        count+=1
print(count)