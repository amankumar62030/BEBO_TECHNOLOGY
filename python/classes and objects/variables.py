
# Variables in Python
# 1.Global
# 2.local--method variable
# 3.instance---class variables(self)


class MyClass:
    a,b = 10,20     #instance variable--class variable
    def add(self):
        # print(a,b)    #is invalid
        print(self.a + self.b)   #need to use self

    def mul(self):
        print(self.a * self.b)

ob1=MyClass()
ob1.add()
ob1.mul()

print("----------Example4----------------")
i,j=13,20   #global
class MyClass1:
    a,b = 19,50     #instance variable

    def add(self,x,y):      #local variable
        print(x,y)      #print local variable
        print(self.a + self.b)      #instance variable
        print(i,j)      #global variable

ob2 = MyClass1()
ob2.add(5,10)



print("----------------Example5----------------------")
r,s = 15,25

class MyClass3:
    r,s = 10,56     #instance variable
    def add(self,r,s):
        print(r,s)      #local variable
        print(self.r + self.s)      #instance variable
        print(globals()['r'],globals()['s'])        #global variable with same name

ob3 = MyClass3()
ob3.add(98,40)
# MyClass3.add(4,5)
