# 1.	Extend the Car class to include a method delete_attribute(attr_name) that checks if the attribute
# exists before deleting it. Print an appropriate message if the attribute does not exist.

class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}, Wheels: {Car.wheels}")

    def delete_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)
            print(f"Attribute '{attr_name}' has been deleted.")
        else:
            print(f"Attribute '{attr_name}' does not exist.")

car1 = Car("Toyota")
car1.show()

car1.delete_attribute("brand")
car1.show()  # This will throw an error since 'brand' no longer exists

car1.delete_attribute("color")
