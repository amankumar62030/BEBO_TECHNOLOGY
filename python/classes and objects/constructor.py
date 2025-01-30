#Constructor in Python

# Constructor name is fixed  def __init--(self)
# Constructor will not return any value
# Constructor can also receive arguments/parameter
# Constructor will be called automatically at the time of object creation.

print("-----------------Default Constructor-----------------")
class MyClass:
    def __init__(self):
        print("I am constructor of the class")
    def m1(self):
        print("Hello, I am the method of the class")
        print(self)    #reference of the object

    def m2(self,a,b):
        return(a+b)

obj = MyClass()     #this will invoke constructor automatically
obj.m1()        #method we have to call explicitly by using object

res=obj.m2(10,20)
print(res)








print("--------------Parameterized Constructor----------------")
class Myclass1:
    name = "David"    #instance variable
    def __init__(self,name):
        print(name)         #local variable
        print(self.name)        #instance variable
obj = Myclass1("Scott")   #at the creation we are passing parameter to the constructor


print("--------------------Example-----------------")
class Employee:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def display(self):
        print(self.eid,self.ename,self.esal)

ob1 = Employee(101,"David",15000)
ob1.display()



print("---------------  __str__(self)  -----------------")
#--str()--() constructor in python used to define the string representation of an object

class MyClass3:
    def __str__(self):
        return "Hello, I am method"
ob3 = MyClass3()
print(ob3)


print("---------------------Example(str)--------------------")
class Employee1:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print(self.eid,self.ename,self.esal)

    def __str__(self):
        return(self.ename)
        # return(self.eid,self.esal)      #invalid


ob1 = Employee1(101,"David",15000)
ob1.display()
print(ob1)



print("-----------------------del----------------")

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}"

c = Car("Tata","Nexon")
print(c.brand)
print(c.model)
print(c)

#deleting the class attribute with del keyword

del c.brand  #trying to access will generate an error
# print(c.brand)  #attributeerror 'Car' object has no attribute 'brand'



#delete an object

del c
# print(c.model)      #NameError: name 'c' is not defined


