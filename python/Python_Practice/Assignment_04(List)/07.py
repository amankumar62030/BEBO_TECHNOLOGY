# 7.Write a Python function that finds and returns the index of all occurrences of a specified element in a list using the index() method. If the element is not found, return None.


my_list = list(map(int,input("Enter the element separated by commas: ").split(",")))
target = int(input("Enter the number to find the index: "))

index =[]

for i in range(len(my_list)):
    if my_list[i]==target:
        index.append(i)

if index:
    print(f"Element present at index {index}")
else:
    print("None")