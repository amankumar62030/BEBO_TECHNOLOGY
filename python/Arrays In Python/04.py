# Reverse an array

import array as arr
numbers = arr.array('i',[])

n = int(input("Enter the number of elements : "))
print("Enter the elements: ")
for _ in range(n):
    elements = int(input())
    numbers.append(elements)
print("original array: ",numbers)
rev_no = arr.array('i',[])
for i in range(n-1,-1,-1):
    rev_no.append(numbers[i])
print("Reversed array: ",rev_no)