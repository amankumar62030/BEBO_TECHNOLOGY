# 3.	Implement a function to check if a number is even or odd and returns a boolean value.

def even_odd(num):
    is_boolean = False
    if num%2==0:
        is_boolean=True
    return is_boolean
num = int(input("Enter the number: "))
print(even_odd(num))
