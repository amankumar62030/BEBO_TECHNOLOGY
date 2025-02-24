# Find the maximum and minimum elements

# import array as arr
# numbers = arr.array('i',[])
# n = int(input("Enter the numbers of elements: "))
#
# print("Enter the elements: ")
# for _ in range(n):
#     elements = int(input())
#     numbers.append(elements)
#
# max_value = numbers[0]
# min_value = numbers[0]
# for i in numbers:
#     if i>max_value:
#         max_value = i
#     if i<min_value:
#         min_value = i
# print(max_value,min_value)


import array as arr
number = arr.array('i',[])
n = int(input("Enter the number of elements:"))

print("Enter the elements:")
for _ in range(n):
    elements = int(input())
    number.append(elements)

max_val = number[0]
min_val = number[0]

for i in number:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i
print(max_val,min_val)