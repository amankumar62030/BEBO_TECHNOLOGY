# 4.	What happens if you pass positional arguments after keyword arguments?

# In Python, positional arguments must come before keyword arguments when calling a function. If you try to pass a positional argument after a keyword argument, Python will raise a SyntaxError.

# def describe_person(name, age, city):
#     print(f"{name} is {age} years old and lives in {city}.")
#
# # Correct: Positional arguments before keyword arguments
# describe_person("Alice", 25, city="New York")
#
# # Incorrect: Positional argument after keyword argument
# describe_person(name="Alice", 25, city="New York")
