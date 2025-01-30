# 12.	Write a lambda function with map to double the elements of a list.

my_list = list(map(int,input("Enter the list of numbers: ").split(",")))

x = list(map(lambda z:z*2,my_list))
print(x)