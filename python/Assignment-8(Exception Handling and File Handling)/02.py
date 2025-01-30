# 2.Create a program that accepts two numbers from the user and divides them. Handle the following exceptions:
# •	ZeroDivisionError if the divisor is zero.
# •	ValueError if the input is not a number.
# •	Any other generic exceptions.


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("ENter second number: "))
    result = num1//num2
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Enter a numeric value")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
