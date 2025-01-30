# A symbol which perform operation between between 2 or more operands

a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)  #quotient
print(a**b)  #5^2

print(3**4)  #81
print(5**3)  #125


# WAP to find out the simple interest
p = 12
r = 2
t = 12

si = ((p*r*t)/100)
print("The simple interest is: ", si)



#wap to print area of circle
# pi = 3.14
# r = 2
#
# result = pi*r*r
# print("Area of circle is: ",result)

# using math module..........................
import math
pi = math.pi
r = 3
result = pi*r**2
print("Area of circle is: ",result)


# Relational operator............................................
# give results in boolean
a = 45  #assignment operator
b = 32

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

print("----------------------------------------------------------------------------------------------------")
#logical operator..........................................
# and, or, not
a = 78
b = 90
print(a==b and a!=b)
print(a==b or a!=b)
print(not a)
print(not b)

