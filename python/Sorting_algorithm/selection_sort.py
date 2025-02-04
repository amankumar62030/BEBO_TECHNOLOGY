# selection sort

my_list = list(map(int, input("Enter the elements separated by commas: ").split(",")))
print("Unsorted list: ",my_list)

for i in range(len(my_list)):
    min_index = i
    for j in range(i+1,len(my_list)):
        if my_list[j] < my_list[min_index]:
            min_index = j

    my_list[i],my_list[min_index]=my_list[min_index],my_list[i]

print("Sorted list:", my_list)


