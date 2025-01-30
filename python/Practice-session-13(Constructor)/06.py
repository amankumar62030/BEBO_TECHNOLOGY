# Create a class Shape with a default constructor that initialize type to "Generic"
class Shape:
    def __init__(self,type = "Generic"):
        self.type = type
    def update_val(self):
        print(self.type)
ob1 = Shape()
ob1.update_val()


