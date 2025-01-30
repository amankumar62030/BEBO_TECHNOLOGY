# 17.	Implement a function to calculate the grade of a student based on marks in five subjects.

def calculate_grade(marks):
    if marks>=90:
        print("The grade is: A")
    elif marks>=80:
        print("The grade is: B")
    elif marks>=50:
        print("The grade is: C")
    elif marks>=30:
        print("The grade is: D")
    else:
        print("Congrats, you are Fail")

marks = int(input("Enter the marks: "))
calculate_grade(marks)