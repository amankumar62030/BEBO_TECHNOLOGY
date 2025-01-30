# 1.	Ask the user for their first name, last name, and age.
# 2.	Concatenate the first name and last name into a single string.
# 3.	Print a greeting message using the concatenated name and age, using an f-string for formatting.
# Example Output:
# Enter your first name: John
# Enter your last name: Doe
# Enter your age: 30
# Hello, John Doe! You are 30 years old.

f_name = input("Enter the first name: ")
l_name = input("Enter the last name: ")
age = int(input("Enter the age: "))

print("Hello,",f_name+" "+l_name,"!",f"You are {age} years old.")