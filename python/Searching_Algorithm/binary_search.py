def binary_search(my_list,target):
    my_list.sort()
    low = 0
    high = len(my_list)-1

    while low<=high:
        mid = (low+high)//2

        if my_list[mid] == target:
            print(f"Element {target} is present at index {mid}")
            break
        elif my_list[mid] < target:
            low =mid+1
        else:
            high =mid-1

    if low>high:
        print("Element is not present")

my_list = list(map(int,input("Enter the element separated by comma: ").split(",")))
target = int(input("Enter the target element: "))
binary_search(my_list,target)



# Binary Search (Only for Sorted Arrays)
# Best Case: O(1) (Middle element is the target)
# Worst Case: O(log n) (Halving the array at each step)
# Average Case: O(log n)
# Space Complexity: O(1) (Iterative) / O(log n) (Recursive due to function call stack)