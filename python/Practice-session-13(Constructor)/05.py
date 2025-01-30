# Create a class Animal and instantiate multiple objects to represent different animals

class Animal:
    def __init__(self,name):
        self.name = name

    def display_info(self):
        print(self.name)

ob1 = Animal("Donkey")
ob1.display_info()
ob2 = Animal("Horse")
ob2.display_info()
ob3 = Animal("Cat")
ob3.display_info()
ob4 = Animal("Dog")
ob4.display_info()