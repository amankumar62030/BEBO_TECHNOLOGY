# 4.	Create a class Student with properties name and marks. Modify and print the updated values.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def modify(self,new_name,new_marks):
        self.name = new_name
        self.marks = new_marks

    def display(self):
        print(f"Name is {self.name} and the marks is {self.marks}")

ob1 = Student("aman",34)
ob1.display()

ob1.modify("Rahul",32)
ob1.display()