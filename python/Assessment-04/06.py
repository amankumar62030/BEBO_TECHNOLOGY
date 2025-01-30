# Return a symmetric difference of two sets

set1 = set(map(int,input("Enter first elements of sets:").split(",")))
set2 = set(map(int,input("Enter second elements of sets:").split(",")))
print(set1 ^ set2)              #first method
print(set1.symmetric_difference(set2))          #second method


