# Write a Python program to demonstrate single inheritance using a Person class and a derived class Employee.



class Person:
    def m1(self):
        print("Class Person")
class Employee(Person):
    def m1(self):
        print("Class Employee")
        super().m1()

ob1 = Employee()
ob1.m1()