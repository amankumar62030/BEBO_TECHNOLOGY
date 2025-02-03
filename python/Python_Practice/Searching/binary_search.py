my_lst = list(map(int, input("Enter the elements of list separated by commas: ").split(",")))
target = int(input("Enter the target element: "))

my_lst.sort()

low = 0
high = len(my_lst) - 1

while low <= high:
    mid = low + high//2

    if my_lst[mid] == target:
        print(f"Element {target} is present at index {mid}")
        break
    elif my_lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if low > high:
    print(f"Element {target} is not present in the list.")


