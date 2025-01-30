# 6.	Write a function safe_divide(a, b) that performs division and raises a custom exception
#DivisionByZeroError if b is zero. Demonstrate its usage with appropriate exception handling.

class DivisionByZeroError(Exception):
    def __init__(self,message="Division by zero is not allowed"):
        super().__init__(message)
def safe_divide(a,b):
    if b==0:
        raise DivisionByZeroError()
    return a/b

try:
    a = int(input("Enter numerator (a): "))
    b = int(input("Enter denominator (b): "))

    result = safe_divide(a, b)
    print(f"Result: {result}")
except DivisionByZeroError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter valid numeric values.")