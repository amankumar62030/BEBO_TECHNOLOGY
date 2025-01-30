from pickle import FLOAT

print(abs(-5))
print(abs(3.5))

print(round(3.1234,2))
print(round(4.23434343,6))
print(round(3.1234))    #3
print(round(3.574857))    #4


print(pow(4,2))    #16
print(4**2)   #16


num = [12,34,56,354,876,31241]
print(min(num))
print(min(45,32))

num = [12,34,56,324,2,7865]
print(max(num))
print(max(78999,32))


print(sum([1,2,3,4]))
num = [12,20]
print(sum(num))

print(divmod(10,3))    #(3,1) 3 (10//3=3)is the quotient and 1(10%3=1) is the remainder as it returning the tuples

a = int(34.2)
print(a)

print(bin(10))
print(hex(10))
print(oct(10))


print(isinstance(5,int))   #True, 5 is the integer
print(isinstance(12.34,int))   #False
print(isinstance(12.34,float))   #True

import math
print(math.factorial(5))

