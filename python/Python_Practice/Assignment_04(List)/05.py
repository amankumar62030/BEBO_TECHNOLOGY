# 5.Write a Python code that removes the minimum and maximum values from a set.

number = set(map(int,input("Enter the element separated by commas: ").split(",")))

min_value = min(number)
max_value = max(number)

for i in number:
    if i<min_value:
        min_value = i
    elif i>max_value:
        max_value = i

print(min_value,max_value)

number.remove(min_value)
number.remove(max_value)
print("Numbers after removing min and max value: ",number)