# implement a Company class with a class attribute company_name. Add instance attribute for employee_name and designation. Create multiple employee and display their details along with the company name


class Company:
    company_name = "Bebo"
    def __init__(self,emp_name,designation):
        self.emp_name = emp_name
        self.designation = designation
    def display(self):
        print(f"employee name={self.emp_name}, Company_name={self.company_name}, designation={self.designation}")

ob1 = Company("David","New York")
ob1.display()
ob2 = Company("Aman","Chandigarh")
ob2.display()