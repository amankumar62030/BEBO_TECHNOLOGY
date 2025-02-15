# 10.	Create a class Grandparent with a method say_hello(). Inherit this class into Parent,
# and then into Child. Demonstrate how the Child class can access methods from Grandparent and Parent.

class Grandparent:
    def say_hello(self):
        print("Hello from Grandparent")
class Parent(Grandparent):
    def say_hello_from_parent(self):
        print("Hello from Parent")
class Child(Parent):
    def say_hello_from_child(self):
        print("Hello from child")

ob1 = Child()
ob1.say_hello()
ob1.say_hello_from_parent()
ob1.say_hello_from_child()