# Create a program to demonstrate how the issubclass() function works with inheritance.

class A:
    print("Class A")

class B(A):
    print("Class B")

class C(A):
    print("Class B")
ob = B()
print(issubclass(B, A))     #true
ob1 = C()
print(issubclass(C,B))      #false
