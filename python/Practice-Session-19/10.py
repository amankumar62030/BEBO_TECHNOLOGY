# Write a program that performs division and uses the finally block to print a cleanup message,
# such as "Execution completed, exiting program," regardless of whether an exception occurs.

def perform_division():
    try:
        number = int(input("Enter the number: "))
        divisor = int(input("Enter the divisor: "))

        result = number/divisor
        print(result)
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Enter numeric value---")
    finally:
        print("Execution completed, exiting program")

perform_division()
