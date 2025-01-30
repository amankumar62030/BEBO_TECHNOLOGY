# Write a program that takes the name of a day as input and checks if it's a weekend. If the day is "Saturday" or "Sunday", print "It's the weekend!". Otherwise, print "It's a weekday".

day = input("Enter the name of the day(from Monday to Sunday: ")

if(day == "Saturday" or day == "Sunday"):
    print("It's Weekend!")
else:
    print("It's not weekend!")