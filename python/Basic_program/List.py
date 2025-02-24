# x = [1,2,3,4]
# y = x
# z = [1,2,3,4]
#
# print(x is y) #true
# print(y is z) #false
# print(x is not y) #false
# print(x is not z) #true


# difference between is and ==
a = 3
b = 4
print(a == b)
print(a is b)
# x == y returns True because the lists contain the same elements.
# x is y returns False because they are two separate list objects in memory.

a = 3
b = a
print(a == b)  #true
print(a is b)   #true

