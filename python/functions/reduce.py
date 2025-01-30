from functools import reduce

z = reduce(lambda x,y:x+y,[1,2,3,4])   #1+2=3,3+3=6,6+4=10
print(z)

