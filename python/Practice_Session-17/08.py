# Write a program to show how the is instance() function can be used with inheritance.


class A:
    def display(self):
        print("Class A")
class B(A):
    def m1(self):
        print("Class B")

ob = B()
print(isinstance(ob,A))
print(isinstance(ob,B))