# 11.	Use a lambda function with filter to extract even numbers from a list of integers.

my_list = list(map(int,input("Enter the list of numbers: ").split(",")))

x = list(filter(lambda z:z%2==0,my_list))
print(x)