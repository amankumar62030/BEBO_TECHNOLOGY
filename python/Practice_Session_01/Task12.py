# Write a program that takes a student's marks as input and determines the grade based on the following criteria:
# •	A: Marks greater than or equal to 90
# •	B: Marks between 80 and 89
# •	C: Marks between 70 and 79
# •	D: Marks between 60 and 69
# •	F: Marks below 60

marks = int(input("Enter the marks of student: "))
if(marks >= 90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
else:
    print("F")