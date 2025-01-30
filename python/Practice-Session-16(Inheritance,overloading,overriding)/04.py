# 4. Create a class Person with attributes name and age. Derive a class Employee from Person that adds
# employee_id and salary Implement methods to display details for both classes.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        super().display()
        print(f"Emp_id: {self.emp_id}  Salary: {self.salary}")

ob1 = Employee("John Doe", 30, 101, 20000)
ob1.display()

