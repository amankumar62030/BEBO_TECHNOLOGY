# Find the sum of elements in array(take input from user


# import array as arr
# numbers=arr.array('i',[10,20,30,40])
# sum = 0
# for i in numbers:
#     sum+=i
# print(sum)


import array as arr
numbers = arr.array('i',[])
n = int(input("Enter the number of elements in the array: "))

print("Enter the elements: ")
for _ in range(n):
    elements = int(input())
    numbers.append(elements)

sum = 0
for i in numbers:
    sum+=i
print(sum)

