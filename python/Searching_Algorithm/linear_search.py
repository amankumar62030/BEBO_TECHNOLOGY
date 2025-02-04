def find_element(my_list,target):
    for i in range(len(my_list)):
        if my_list[i]==target:
            print(f"Element {target} is present at index {i}")
            break
    else:
        print(f"Element {target} is not present in the list")

my_list = list(map(int,input("Enter the element separated by commas: ").split(",")))
target = int(input("Enter the target element :"))
find_element(my_list,target)


# Linear Search
# Best Case: O(1) (Element found at the beginning)
# Worst Case: O(n) (Element found at the end or not present)
# Average Case: O(n)
# Space Complexity: O(1) (No extra space required)