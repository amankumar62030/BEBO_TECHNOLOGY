my_list = list(map(int, input("Enter the elements separated by commas: ").split(",")))
print("Unsorted list: ",my_list)

for i in range(len(my_list)):
    for j in range(0, len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print("Sorted List:", my_list)
