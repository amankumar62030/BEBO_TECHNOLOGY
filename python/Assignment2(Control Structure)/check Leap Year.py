# # Leap Year Checker: Create a function that takes a year as input and determines if it's a leap year. A year is a leap year if:
#
# year = int(input("Enter the Year:"))
#
# if(year%400==0):
#     print("Leap Year")
# elif(year%100==0):
#     print("Not a Leap Year")
# elif(year%4==0):
#     print("Leap Year")
# else:
#     print("Not a Leap year")

year = int(input("Enter the year: "))
if year%400==0:
    print("Lear Year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not a leap year")
