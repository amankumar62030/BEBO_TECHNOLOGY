# 11.Write a program that demonstrates the error if positional arguments are placed after keyword arguments.

def greet(name, message):
    print(f"{message}, {name}!")

# Incorrect: Positional argument after keyword argument
# greet(message="Hello", "Alice")  # This will cause an error


