# Write a Python function that takes two sets and returns the difference between the two sets

my_set1 = set(map(int,input("Enter the elements of set1: ").split(",")))
my_set2 = set(map(int,input("Enter the elements of set2: ").split(",")))

print(my_set1 - my_set2)
print(my_set1.difference(my_set2))