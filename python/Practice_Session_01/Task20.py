# Write a program that takes two values from the user. Check if:
# •	Both values are positive or if both values are negative.
# •	If they are mixed (one positive and one negative), print "Mixed signs".

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if(a>0 and b>0):
    print("Both values are positive!")
elif(a<0 and b < 0):
    print("Both values are negative!")
else:
    print("Mixed signs")