# 16.	Write a function that takes a list of numbers and returns both the maximum and minimum numbers.

def max_min(my_list):
    # return max(my_list),min(my_list)
    max_value=my_list[0]
    min_value=my_list[0]
    for i in my_list:
        if max_value>i:
            max_value=i
        if min_value<i:
            min_value=i
    return max_value,min_value
my_list = list(map(int,input("Enter the list of numbers: ").split(",")))
print(max_min(my_list))