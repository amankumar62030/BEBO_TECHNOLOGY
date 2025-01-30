# 4.	Write a function find_maximum that takes three numbers as parameters and returns the largest
# of the three. Demonstrate the function with an example.

# def find_maximum(n1,n2,n3):
#     return max(n1,n2,n3)
#
# n1 = int(input("Enter first number:"))
# n2 = int(input("Enter second number:"))
# n3 = int(input("Enter third number:"))
# print("The maximul number is: ",find_maximum(n1,n2,n3))

# -----------------------------------------------------------------------------------------------------
# 5.	Explain positional and keyword arguments in Python functions. Provide a code example
# that includes both types of arguments.
'''
Positional Arguments
Arguments are passed in the order in which they are defined in the function.
The function matches arguments to parameters based on their position.
Keyword Arguments
Arguments are passed by explicitly specifying the parameter name along with its value.
This allows arguments to be passed in any order.
'''
# def describe_person(name, age, city="Unknown"):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")
#
# # Using positional arguments
# describe_person("Aman", 20)
#
# # Using only keyword arguments
# describe_person(name="Rahul", city="Mumbai", age=30)

# -------------------------------------------------------------------------------------------------------
# 6.Create a function personal_info that takes a name and age as positional arguments and an optional
# keyword argument city. If the city argument is not provided, the function should assume the city is
# "Unknown". Write sample calls for each possible way of calling this function.

# def personal_info(name, age, city="Unknown"):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")
#
# # Using positional arguments
# personal_info("Aman", 20)
# #mixing both
# personal_info(name="Rahul", age=30, city="Mumbai")
# #using keyword
# personal_info(name="Rahul", city="Mumbai", age=30)

# ----------------------------------------------------------------------------------------------------------
# 7.	Write a function sum_of_squares that accepts any number of arguments and returns the sum of the
# squares of each argument. Demonstrate how you would call this function with varying numbers of arguments.

def sum_of_square(*n):
    total = 0
    for i in n:
        total += i**2
    return total
n = int(input("Enter the number: "))
print(sum_of_square(1,2,3))
print(sum_of_square(2,4))
