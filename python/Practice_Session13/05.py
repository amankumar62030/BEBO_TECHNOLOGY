# 5.	Create a class Animal and instantiate multiple objects to represent different animals.

class Animal:
    def __init__(self,name , sound):
        self.name = name
        self.sound = sound

    def display(self):
        print(f"Animal {self.name} sounds {self.sound}")

dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")
cow = Animal("Cow", "Moo")
dog.display()
cat.display()
cow.display()