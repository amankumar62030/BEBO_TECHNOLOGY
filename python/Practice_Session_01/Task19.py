# Write a program that checks if a person is eligible to drive. The criteria are:
# •	The person must be at least 18 years old and have a valid driver's license.


age = int(input("Enter the age of a person: "))

if(age>=18):
    print("Eligible to drive!")
else:
    print("Not eligible to drive!")