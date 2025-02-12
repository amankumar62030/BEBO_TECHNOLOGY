# 4.	Create two parent classes, Person and Employee. The Person class should have attributes name and
# age, and the Employee class should have an attribute salary. Create a child class Manager that inherits
# from both and includes an additional attribute department.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, age, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}")

manager = Manager("John Doe", 40, 80000, "HR")
manager.display_info()
