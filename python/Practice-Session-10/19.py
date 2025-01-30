# 19.	Create a function to generate a random password with a given length, ensuring a mix of uppercase, lowercase, digits, and special characters.


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter the password length: "))
print("Generated password:", generate_password(length))