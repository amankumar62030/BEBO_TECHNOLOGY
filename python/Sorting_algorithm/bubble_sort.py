my_list = list(map(int,input("Enter the element separated by commas: ").split(",")))
print("Unordered list: ",my_list)

for i in range(len(my_list)):
    for j in range(len(my_list)-1):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]

print("Sorted using bubble sort: ",my_list)