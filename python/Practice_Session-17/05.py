# Write a Python program to demonstrate how super() can be used to call a parent class
# constructor.


class A:
    def __init__(self):
        print("Constructor of Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of Class B")
    def m1(self):
        print("Method m1 of Class B")
ob = B()
ob.m1()
