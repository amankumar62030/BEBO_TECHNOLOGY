# 8.	Create a class Employee that overrides __str__ to format the details.

class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id  = id

    def __str__(self):
        return f"{self.name} and {self.id}"

ob = Employee("aman",32)
print(ob)