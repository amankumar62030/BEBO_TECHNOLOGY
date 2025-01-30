# Create a class Student with properties name and marks. Modify and print the updated value

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def updated_val(self,new_name, new_marks):
        self.name = new_name
        self.marks = new_marks
    def display_val(self):
        print(f"The updated name is {self.name} and the updated marks is {self.marks}")

ob1 = Student("Satwinder",234)
ob1.display_val()
ob1.updated_val("Aman",749)  # Updated name and marks
ob1.display_val()
