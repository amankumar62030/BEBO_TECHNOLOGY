# Create a program that accepts two integers from the user. Handle the case where the user
# enters a non-integer value using ValueError.

def two_integer(a, b):
    print(f"Value of a: {a}")
    print(f"Value of b: {b}")

try:
    a = int(input("Enter an integer for a: "))
    b = int(input("Enter an integer for b: "))
    two_integer(a, b)
except ValueError:
    print("Error: Please enter valid integers.")
