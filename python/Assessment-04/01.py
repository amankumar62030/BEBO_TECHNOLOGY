# Write a Python code that takes a list of numbers as input and removes all occurrences of a specified number using the remove() method. Return the modified list.

def remove_all_occurrences(numbers, target):
    while target in numbers:
        numbers.remove(target)
    return numbers

numbers = list(map(int, input("Enter the list of numbers separated by commas: ").split(",")))
target = int(input("Enter the number to remove: "))
modified_list = remove_all_occurrences(numbers, target)
print("Modified list:", modified_list)
