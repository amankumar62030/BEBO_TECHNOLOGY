# Create a class car and print a message when an object is deleted

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(self.brand,self.model)
obj1 = Car("TATA","NEXON")
obj1.display_info()

del obj1
print("obj1 is successfully deleted ---")
# obj1.display_info()         #NameError: name 'obj1' is not defined
