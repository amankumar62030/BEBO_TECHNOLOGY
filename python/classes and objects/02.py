# Two types of methods in python

class Myclass:
    def m1(self):
        print("This is the instance method")
    @staticmethod
    def m2(num):    #static method dont take self parameter cause it is not bound to an instance
        print(num)

ob1 = Myclass()
ob1.m1()
ob1.m2(32)
Myclass.m2(67)      #we can call static method with class name
# Myclass.m1()      #we cant call instance method with class name