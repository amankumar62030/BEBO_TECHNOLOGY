def greatest_of_two_num(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("The greatest of two number is: ",greatest_of_two_num(a,b))