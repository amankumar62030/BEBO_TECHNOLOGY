# 1.	Define a variable, assign it any value, and print it.
# 2.	Delete the variable using the del keyword.
# 3.	Try printing the variable after deletion and observe the error.
# Example Output:
# Before deletion: This variable will be deleted
# After deletion: NameError: name 'temp_var' is not defined


a = 234
print("This variable will be deleted: ",a)

del a

print(a)
