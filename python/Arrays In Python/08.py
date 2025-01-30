# Remove duplicates from array

import array as arr
numbers = arr.array('i',[])
n = int(input("Enter the number of elements:"))
print("Enter the elements:")
for _ in range(n):
    elements = int(input())
    numbers.append(elements)

i = 0
while(i<len(numbers)):
    j = i+1
    while(j<len(numbers)):
        if numbers[i]==numbers[j]:
            numbers.pop(j)
        else:
            j+=1
    i+=1
print(numbers)