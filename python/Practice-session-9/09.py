# 9.	Write a program to display a person’s details using keyword arguments.


def person_details(name, city,address):
    return name,city,address

name = input("Enter name:")
city = input("Enter city:")
address = input("Enter address:")
print(name,city,address)

print(person_details(name=name, city=city, address=address))