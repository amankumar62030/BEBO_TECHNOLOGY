# Search for an element in array

import array as arr
numbers = arr.array('i',[])
n = int(input("Enter the number of elements: "))

print("Enter elements: ")
for _ in range(n):
    elements = int(input())
    numbers.append(elements)
print("Original array: ",numbers)

search = int(input("Enter the elements to search: "))
found = False
for i in range(n):
    if numbers[i]==search:
        print(f"Element {search} found at index {i}")
        found=True
        break
if not found:
    print("Elements not found...")