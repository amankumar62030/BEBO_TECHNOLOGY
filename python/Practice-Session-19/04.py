# Create a program with a dictionary of fruits and their prices. Allow the user to input
# a fruit name and display its price. Handle the case where the fruit does not exist using KeyError.


fruits = {"apple": 100, "banana": 30, "mango": 50}
try:
    fruit = input("Enter the fruit: ")
    print(fruits[fruit])
except KeyError:
    print("Fruit not found.")