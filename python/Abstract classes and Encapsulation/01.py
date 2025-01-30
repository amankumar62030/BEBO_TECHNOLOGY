# Abstract classes are the classes that cannot be instantiated on their own and are meant to be sub classed
# They serve as blueprint for other classes, ensuring that certain methods are implemented in any subclass


# Abstract base classes(ABCs) in Python
# ABCs are classes that provide a way to define abstract methods and properties


# from abc import ABC,abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def display(self):
#         None
# class B(A):
#     def display(self):
#         print("Hello, i am concrete class now")
#     def display2(self):
#         print("hey, i am display method")
#
# class C(B):
#     def student(self):
#         print("hi")
#     def name(self):
#         print("i am python")
#
# ob = C()
# ob.display2()
# ob.student()

# ob1 = A()       #we cannot crete object of the abstract class
# ob1.display()

# ---------------------------------------------------------------------------------------------------

# from abc import ABC, abstractmethod
# class Animal(ABC):     #what to do, how to eat
#     @abstractmethod
#     def eat(self):
#         pass
# class Tiger(Animal):
#     def eat(self):
#         print("Eat non-veg")
# class Cow(Tiger):
#     def eat(self):
#         print("Eat only-veg")
#
# c = Cow()
# c.eat()
#
# t = Tiger()
# t.eat()



# --------------------------------------------------------------------------------------------------
# Task---Shape--ABC area,perimeter(abstractmethod())
#Rectangle(Shape)--area,perimeter

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def rectangle(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)
    def perimeter(self):
        print(2 * (self.length + self.width))

rect = Rectangle(5, 3)
rect.area()
rect.perimeter()


