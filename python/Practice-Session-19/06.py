# Write a program that combines multiple operations, such as dividing two numbers and retrieving
# an element from a list. Use nested try-except blocks to handle specific exceptions like ZeroDivisionError
# and IndexError

def perform_operations():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        try:
            result = numerator / denominator
            print(f"Division Result: {result}")
        except ZeroDivisionError as e:
            print(e)

        elements = [10,20,30,40]
        print(f"List: {elements}")

        index = int(input("Enter the index to retrieve the element: "))
        try:
            elements = elements[index]
            print(f"Retrieved Element: {elements}")
        except IndexError:
            print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
perform_operations()