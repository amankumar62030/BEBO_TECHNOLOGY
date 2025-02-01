# 1.Write a Python code that takes a list of numbers as input and removes all occurrences of a specified number using the remove() method. Return the modified list.

def occurance_of_no(number,target):
    while target in number:
        number.remove(target)
    return number


number = list(map(int,input("Enter the number separated by commas: ").split(",")))
target = int(input("Enter the number to remove: "))
modified_ele = occurance_of_no(number,target)
print(modified_ele)

