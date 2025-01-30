# Develop a Laptop class with attribute like brand and model. Use a constructor to initialize these attributes. Include a method specifications() to print the details


class Laptop:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def specification(self):
        print(f"Model={self.model},Brand={self.brand}")
ob1 = Laptop("Vivobook","Asus")
ob1.specification()