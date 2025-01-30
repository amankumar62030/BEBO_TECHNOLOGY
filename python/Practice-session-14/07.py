# Write a python program to implement an Employee class with a constructor that initialize id, name and salary. Add a method give_raise(percent) to increase salary by a given percentage.

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        raise_amount = (self.salary * percent) / 100
        self.salary += raise_amount
        print(f"The salary of {self.name} after a {percent}% raise is: {self.salary}")


emp1 = Employee(101, "John Doe", 50000)
emp1.give_raise(10)

