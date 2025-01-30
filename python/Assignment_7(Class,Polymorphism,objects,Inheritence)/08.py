# 8.	Write a function describe_pet() that accepts an object and calls the speak() method on it. Create
# two classes, Parrot and Fish, where only the Parrot class has a speak() method. Pass objects of both
# classes to describe_pet() and observe the behavior.

class Parrot:
    def speak(self):
        print("Parrot says: Squawk!")

class Fish:
    pass

def describe_pet(pet):
    try:
        pet.speak()
    except AttributeError:
        print(f"{pet.__class__.__name__} cannot speak.")

parrot = Parrot()
fish = Fish()

print("Describing a Parrot:")
describe_pet(parrot)

print("\nDescribing a Fish:")
describe_pet(fish)
