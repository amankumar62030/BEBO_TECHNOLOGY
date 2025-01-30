
#strings are immutable
# name = "aman"
# print(name)
# name[0] = "rohit"
# print(name)  #TypeError: 'str' object does not support item assignment


# print(id(name))   #print the reference(location)
#
# name = name+"hello"
# print(id(name))


# a="aman"
# b="aman"
# print(id(a))   #2394799343728   #referencing to the same memory location
# print(id(b))   #2394799343728


# str = "hello"
# str2 = str + ",World"
# print(str2)
#
# #print no. of times
# print(str*2)             #hellohello
# print(str2*4)            #hello,Worldhello,Worldhello,Worldhello,World


# s = 'welcome'
# s = "welcome"
# s = str("welcome")
# s = str('welcome')


# create an empty string
# n = ''
# n = ""
# n = str()
# type(n)


#slicing..............................................

str = "welcome"
# print(str[1:4])  #elc
# print(str[:4])  #welc
# print(str[0:])  #welcome
# print(str[1:-1])    #elcom, remove last 1 character
# print(str[1:-2])    #elco, remove last 2 character
# print(str[-2])    #m, it will give second last element
# print(str[-4:-1])   #com




# ord() ---return the ASCII value of the character
#chr( ------return the character value

a = "a"
print(ord(a))
print(ord("A"))

a = 97
print(chr(a))
print(chr(65))


print(max("abc"))   #c
print(max("pqr"))   #r
print(min("abc"))    #a
print(min("xyz"))    #x

print(len("welcome"))     #7
print(len("hello world"))   #11,includes the space



# in, not operator...................................
# it is case sensetive
s = "welcome"
print("come" in  s)   #true
print("Come" in s)  #false
print("come" not in s)    #false
print("kdi" not in s)   #true



# String comparison.............................
#it compares the ASCII value
print("hello" == "world")   #false
print("Hello" != "world")   #true
print("arrow" > "aron")     #True
print("right" >= "left")  #true
print("teeth" < "tee")      #false
print("abc" > "")   #true
print("aman" > "satwinder")   #false
print("aman" > "sunil")     #false
print("sunil" > "satwinder")   #True

