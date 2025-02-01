my_lst = list(map(int,input("Enter the elements of list separated by commas: ").split(",")))
target = int(input("Enter the target element: "))

for i in range(len(my_lst)):
    if target in my_lst:
        print(f"The element {target} is present in the list")
        break
    else:
        print(f"The element {target} is not present in the list")
        break