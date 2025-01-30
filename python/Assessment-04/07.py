# Write a python function that finds and return the index of all occurances of a specified element in a list using the index() method. If the elements is not found, return none

# def index_of_all_occurances(my_list,find):
#     update_list = []
#     for i in my_list:
#         if find not in my_list:
#             return None
#         else:
#             return update_list.append(i)
#
#
#
# my_list = list(map(int,input("Enter the elements of list:").split(",")))
# find = int(input("Enter elements to find:"))
# result =  index_of_all_occurances(my_list,find)
# print(result)


my_list = list(map(int, input("Enter the elements of the list separated by commas: ").split(",")))
target = int(input("Enter the element to find: "))
indices = []

for i in range(len(my_list)):
    if my_list[i] == target:
        indices.append(i)

if indices:
    print(f"Element found at indices: {indices}")
else:
    print("Element not found.")

