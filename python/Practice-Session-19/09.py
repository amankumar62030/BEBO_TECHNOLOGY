# Write a program that accepts two inputs: a number and its divisor. Handle multiple exceptions,
# such as ZeroDivisionError (if the divisor is zero) and ValueError (if non-numeric inputs are provided).

def divide_numbers():
    try:
        number = float(input("Enter the number: "))
        divisor = float(input("Enter the divisor: "))

        result = number / divisor
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
divide_numbers()
