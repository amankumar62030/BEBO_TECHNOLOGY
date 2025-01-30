
s = "hello world"
print(s.isalnum())      #false
print(s.isalpha())      #false,cause it contains the spaces

s = "helloworld"
print(s.isalnum())     #true


s = "hello123"
print(s.isalnum())  #true
print(s.isalpha())  #false,cause it not containing number only

s = "abx123"
print(s.isdigit())
s = "123"
print(s.isdigit())

s = "welcome to python"
print(s.isidentifier())

r = "Hello World"
print(r.islower())
print(r.isupper())

r = "Hello World"
print(r.endswith("rld"))   #true
print(r.startswith("Hell"))   #true

print(r.find("Hello"))      #give index
print(r.find("World"))

print("hcome".find("hello"))      #-1

s = "hello world"
print(s.count("o"))



s = "string in python"

print(s.capitalize())    #String in python

print(s.title())    #String In Python

print(s.lower())    #string in python

print(s.upper())   #STRING IN PYTHON

print(s.swapcase())    #convert lower into upper, and upper into lower


a = "hello World"
print(a.replace("lo","lllloooo"))
print(a.replace("World", "Guyzzzz"))




print("---------------------STRING REVERSE----------------------------------")
#1st method

b = "welcome"
rev_str=""

for i in b:
    rev_str = i+rev_str
print(rev_str)


#2nd Method

s = "welcome"
print(s[::-1])








