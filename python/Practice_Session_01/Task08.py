# 1.	Ask the user to input a number as a string.
# 2.	Convert this input to an integer and print the result along with its type.
# 3.	Try converting it to a float and print the result with its type.
# Example Output:
#
# Enter a number: 25
# Integer: 25, Type: <class 'int'>
# Float: 25.0, Type: <class 'float'>

a = input("Enter a number:")
int_value = int(a)
print("Integer:",int_value, "Type:",type(int_value))
float_value = float(a)
print("Float:", float_value, "Type:",type(float_value))
