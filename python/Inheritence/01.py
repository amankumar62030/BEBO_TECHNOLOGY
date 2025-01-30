

# Example............1(Single Inheritance)

# class A:
#     def __init__(self):
#         print("I am Constructor")
#     def m1(self):
#         print("Hii, I am method from class A")
#
# class B(A):
#     def __init__(self):
#         print("i am constructor from B")
#     def m2(self):
#         print("Hii, I am method from class B")
#
# Bobj = B()
# Bobj.m2()
# Bobj.m1()


# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
# ob1 = B()
# ob1.m1()
# ob1.m2()


# Example............3(Multilevel Inheritance)

# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def __init__(self):
#         print("I am the constructor of B")
#     def m2(self):
#         print(self.a+self.b)
#
# class C(B):
#     i,j=20,40
#     def __init__(self):
#         print("I am the constructor of C")
#     def m3(self):
#         print(self.i+self.j)
#
# ob1 = C()
# ob1.m1()
# ob1.m2()
# ob1.m3()


# Example............4(Heirarchy Inheritance)
# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def __init__(self):
#         print("I am the constructor of B")
#     def m2(self):
#         print(self.a+self.b)
#
# class C(A):
#     i,j=20,40
#     def __init__(self):
#         print("I am the constructor of C")
#     def m3(self):
#         print(self.i+self.j)
#
# ob1 = C()
# ob1.m1()
# ob1.m3()
#
# ob2 = B()
# ob2.m1()
# ob2.m2()


# Example............5(Multiple Inheritance)
# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=100,200
#     def __init__(self):
#         print("I am the constructor of B")
#     def m2(self):
#         print(self.a+self.b)
#
# class C(A,B):
#     i,j=20,40
#     def __init__(self):
#         print("I am the constructor of C")
#     def m3(self):
#         print(self.i+self.j)
#
# ob1 = C()
# ob1.m1()
# ob1.m2()


# class A:
#     def print(self):
#         print("This is print method from class A")
#
# class B:
#     def print(self):
#         print("This is print method from class B")
#
# class C(A,B):
#     i,j=20,40
#     def __init__(self):
#         print("I am the constructor of C")
#     def m3(self):
#         print(self.i+self.j)
#
# ob1 = C()
# ob1.print()


# Example............6(Method Overriding)
# class A:
#     def print1(self):
#         print("This is print method from class A")
#
# class B(A):
#     def print1(self):
#         print("This is print method from class B")
#         super().print1()   #invoke immediate parent class method; calling parent class
#     def print(self):
#         print("Hii All")
#
# ob1 = B()
# ob1.print1()            #This is the method from B


# class A:
#     name = "Satwinder"
# class B(A):
#     name = "Aman"
#     def test(self):
#         print(super().name)
#
# ob = B()
# print(ob.name)
# ob.test()



#Example-8-------------how to access the parent class variables
# a,b=1000,2000
# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m1(self,x,y):
#         print(x+y)      #30
#         print(self.i+self.j)    #300
#         print(globals().a + globals().b)      #30000
# ob = B()
# ob.m1()



# Overloading..............................
# class cal:
#     def m(self):
#         print("Hello")
#     def m(self,x,y):
#         print(x+y)
# obj = cal()
# obj.m()
# obj.m(10,20)

# class Human:
#     def sayHello(self,name = None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("Hello")
# obj = Human()
# obj.sayHello()
# obj.sayHello("aman")


class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal = Calculation()
cal.add()
cal.add(10,20)
cal.add(10,20,30)