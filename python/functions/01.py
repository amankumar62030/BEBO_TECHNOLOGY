# Functions in python are reusable blocks of code designed to perform a specific tasks.
# They make programs modular, easy to understand, and maintainable.
# Functions can take input, perform operations and return outputs.
from inspect import Arguments

# ..................Key benefits..................
# Code reusability
# Improved readability
# Easier debugging

print("-----------------Example1-------------------")
def myfunc():          #declaring the functions
    print("Hello")
myfunc()            #calling the functions


#parameter/arguments------>optional


print("--------------Example2--------------")
def myfun(name):
    print("Hello",name)

myfun("Aman")



print("------------------Example3-----------------")
def cal(a,b):
    return (a+b)
print(cal(10,20))
# sum = cal(10,30)
# print(sum)


print("---------------------Example4--------------------")
def fun():
    return
print(fun())        #None

def fun(i):
    i = 10
print(fun(10))      #None



print("---------------Example5------------------")
def cal(a,b):
    print(a+b)
cal(10,20)
# --------------------------------------------------------------
def cal(a,b):
    return (a+b)
print(cal(20,40))


# Types of function--------------------------------------
# function does not argument not return any value (None)
# function does not take argument but return some value
# function takes argument but no return value   (print)
# function takes argument and also return value


print("----Add two number using functions..............")
def sum(a,b):
    return (a+b)
print(sum(10,20))

print("----Factorial..............")
def fact(n):
    fact =1
    for i in range(1,n+1):
        fact*=i
    return fact
# n = int(input("Enter the number:"))
print(fact(3))



print("------------------global and local variables-------------------")
print("...................example1------------")
global_var=20   #global variable
#Global variable can be accessed outside the function
def func():
    local_var=10    #local variable
    print(local_var)

print(global_var)
# print(local_var)    #Invalid
func()
#local variable cannot be accessed outside the function


print("----------Exampl2-->>when local and global variable have same name-----------")

xy = 100
def cool():
    xy = 200
    print(xy)
cool()
print(xy)

print("-----Example3-->Requirement is we want to change the value of global variable inside func...")
xy = 100
def cool():
    global xy       #global is keyword
    xy = 200        #global variable
    print(xy)       #200
cool()      #200
print(xy)       #200


print("----------using global variable in func to update the value--------")
x = 100
def cool():
    global x
    x = 500
    print(x)
cool()      #500
print(x)        #500



print("-------it is not mandatory to declare global variable outside the func ............")
def cool():
    global x
    x = 500
    print(x)
cool()
print(x)



# ---------------Arguments----------------------
# Positional arguments
# Keyword arguments
# default arguments
# Variable length arguments
# Keyword-only-variable-length argumnets


print("------------Example1-------")
def fun(i,j):
    print(i,j)
fun(10,20)      #positional
fun(i=10,j=30)      #keyword
fun(j=20,i=10)      #keyword


print("---------Example2-->default value assigned to positional agrumnets--------")
def fuc(i,j=200):
    print(i,j)
fuc(10,20)
fuc(100)


print("-----Example3--------")
def greeting(name,greetmsg):
    print(greetmsg+" "+ name)

greeting("John","hello")    #positional
greeting(name ="John",greetmsg="hello")     #keyword
greeting(greetmsg="John",name="hello")      #keyword


print("-----------------Example4------------")
def func(a,b,c):
    print(a,b,c)

func(10,20,30)      #positional
func(a=10,b=20,c=30)        #keyword
func(b=20,a=10,c=30)        #keyword
print("-----------#we can also take the combination of both types-----------")
func(10,20,c=30)    #valid
func(10,b=20,c=30)      #valid
# func(10,b=20,30)    #Invalid cause positional agrumnet must appears before any keyword argumnet
# func(10,30,b=20)    #logical error


print("--------------lamda function----------------")

# function which has no name
# This is also called as anonymous func.
# Syntax:
# lamda arguments:expression

# from functools import reduce

x = lambda a:a+10
print(x(5))

x = lambda a,b:a+b
print(x(5,5))

x = lambda a,b,c:a+b+c
print(x(10,10,20))



# variable argument
# *args --->positional variable length argument
# **kwargs --->keyword variable length argument
# allow a function to accept any no. of positional argument
# which will be passed as a tuple to the function
# sum(10,20)
# sum(10,20,30,40)

print("------------------------Variable Length arguments-----------------")
print("----------Example1--------------")
def greet(*name):
    print("Hello",{name})
greet("David")
greet("David","John","Merry","Bob")


print("----------Example2(keyword argument)--------------")

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
student_info(name="aman",id=101)



print("------------Example3(using both args and kwargs)-------------------------")
def display_info(*args,**kwargs):
    print("Positional argument:",args)
    print("Keyword argument:", kwargs)
display_info(1,2,3,name="Aman",age=22,id=101,city="Chandigarh")




print("--------------------Example4--------------------")
def greet(name,*args):
    print(name,args)
greet("John","David","Bob",30,True,32.5)


print("--------------------Example5--------------------")
def greet(name,*args,**kwargs):
    print("Default agrument:",name)
    for i in args:
        print("Positional argument:",i)
    for  i,j in kwargs.items():
        print(f"{i}:{j}")
greet("John","Rohan",30,34.5,name1="Sohit",age=31,City="Chandigarh")




def sum(*name):
    print("Hello",name)
sum("a","b","c")