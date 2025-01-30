# 3. Write a Python program where a class Animal has a method make_sound). Create subclasses Dog,
# Cat, and Cow that override the make_sound method to print their respective sounds.


class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    print("bhaw bhaw")
class Cat(Animal):
    print("meoww")
class Cow(Animal):
    print("maaaaaaaa")


ob1 = Dog()
ob2 = Cat()
ob3 = Cow()

ob1.make_sound()
ob2.make_sound()
ob3.make_sound()