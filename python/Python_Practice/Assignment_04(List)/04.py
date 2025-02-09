# 4.Write a Python code that converts a tuple of numbers to a list, appends a given number to the list, and then converts it back to a tuple.


tuple1 = {12,34,56,78}
list1 = list(tuple1)
print(type(list1))
list1.append(900)
list2 = tuple(list1)
print(list2)
print(type(list2))