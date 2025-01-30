# Write a function called min_max_tuple that takes a tuple of integers and returns a tuple containing the minimum and maximum values from the input tuple.
#
# Input: min_max_tuple((4, 1, 8, 3, 9))
# Output: (1, 9)


# def min_max_tuple(n):
#     return min(n),max(n)
#
# user_input = tuple(map(int, input("Enter the elements of tuple: ").split(",")))
# print("Tuples are : ", user_input)
# result = min_max_tuple(user_input)
# print("Min and Max are: ",result)

user_input = tuple(map(int, input("Enter the elements of tuple: ").split(",")))
min_value = user_input[0]
max_value = user_input[0]

for i in user_input:
    if i<min_value:
        min_value=i
    elif i>max_value:
        max_value=i
print(min_value,max_value)




