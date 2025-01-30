# Write a program that asks for a person's age and checks if they are eligible to vote. The voting age is 18 or above.

age = int(input("Enter the age of a person: "))

if(age>=18):
    print("Eligible to vote")
else:
    print("not eligible to vote")