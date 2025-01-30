# Write a function called second_largest that takes a list of integers and returns the second largest number.

def second_largest(n):
    s = sorted(l1)
    max_val = s[-1]
    for i in reversed(s):
        if i<max_val:
            print(i)
            break

l1 = list(map(int, input("Enter the elements of list: ").split(",")))
result = second_largest(l1)
print(result)