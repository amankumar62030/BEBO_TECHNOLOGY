# Find the frequency of each element


import array as arr
numbers = arr.array('i',[])
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for _ in range(n):
    elements = int(input())
    numbers.append(elements)
print("Original array:",numbers)

freq = {}
for i in numbers:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i]+=1
# print(freq)

print("Frequencies of elements:")
for num, count in freq.items():
    print(f"Element {num}: {count}")
