# Write a program that accepts a list of integers from the user and retrieves an element by index.
# Handle the case where the index is out of range using Index Error.

def my_list(l1):
    print(l1)
try:
    l1 = list([int(e) for e in input("Enter the number of list separated by comma : ").split(",")])
    my_list(l1)

    indx = int(input("Enter the index: "))
    print(l1[indx])

except IndexError as e:
    print(e)
