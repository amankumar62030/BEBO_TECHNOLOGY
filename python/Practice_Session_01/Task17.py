# Write a program that checks if a student is eligible for admission to a specific course. The criteria for eligibility are:
# •	The student must have scored at least 80% in math and 70% in science.
# •	Or they must have a total average score of at least 75%.


sub1 = int(input("Enter the marks of Maths: "))
sub2 = int(input("Enter the marks of Science: "))


average = ((100)*(sub1+sub2)/200)

if(average >= 75 or sub1>=80 and sub2>=70):
    print("you are pass: ",average)

else:
    print("You fail: ",average)