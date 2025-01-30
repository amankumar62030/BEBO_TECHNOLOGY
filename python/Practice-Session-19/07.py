# Create a custom exception class called InvalidAgeException. Write a program that raises
# this exception if the user inputs an age less than 18.


class InvalidAgeException(Exception):
    def __init__(self, message="Age must be at least 18"):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise InvalidAgeException
    print("Good Age")

try:
    age = int(input("Enter age: "))
    check_age(age)
except InvalidAgeException as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")
