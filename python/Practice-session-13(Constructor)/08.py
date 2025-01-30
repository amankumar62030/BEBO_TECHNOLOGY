# Create a class Employee that overrides __str__ to format the details

class Employee:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return f"{self.eid, self.ename,self.esal}"

obj1 = Employee(101,"David",12909)
print(obj1)