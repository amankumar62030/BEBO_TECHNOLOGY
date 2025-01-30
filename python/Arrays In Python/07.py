# sort an array

import array as arr
numbers = arr.array('i',[12,5,6,23,78,43])
print("Before sort",numbers)
#Bubble sort algorithm
n = len(numbers)
for i in range(n):
    for j in range(0,n-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print("After sort",numbers)


# s=sorted(numbers)
# print(s)