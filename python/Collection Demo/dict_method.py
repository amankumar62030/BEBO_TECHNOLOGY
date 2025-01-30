print(".........key() method---------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
print(my_dict.keys())  #return the object of all the keys/only set of values


print(".........values() method---------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
print(my_dict.values())

print(".........items() method---------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
print(my_dict.items())


print(".........update() method---------------------")
my_dict1 = {"name":"aman","age":22,"Address": "Chandigarh"}
my_dict2 = {"dept":101,"city":"NEW YORK"}
my_dict2.update(my_dict1)
print(my_dict2)


print(".........copy() method---------------------")
my_dict1 = {"name":"aman","age":22,"Address": "Chandigarh"}
my_dict2 = my_dict1.copy()
print(my_dict2)



print(".........fromkeys() method---------------------")
# create the copy of dictionary with specified keys and a single value

keys = [1,2,3]
default_value = "welcome"
my_dict = dict.fromkeys(keys,default_value)
print(my_dict)



print(".........setdefault() method---------------------")
# return the value of a key if it is in the dictionary
# if not, it inserts the key with the specified default value
my_dict1 = {"name":"aman","age":22,"Address": "Chandigarh"}
my_dict1.setdefault("age",30)
print(my_dict1)
my_dict2 = {"name":"aman","Address": "Chandigarh"}
my_dict2.setdefault("age",30)
print(my_dict1)



print("-------------using for loop--------------------")
my_dict1 = {"name":"aman","age":22,"Address": "Chandigarh"}
for keys, values in my_dict1.items():
    print(f"{keys}:{values}")



print("----------dictionary comprehension------------")
# {0:0,1:1,2:4,3:9,4:16}

square = {x:x**2 for x in range(0,11)}   #o,1,2,3,4
print(square)




print("--------------Nested dictionary--------------------")
my_dict = {
    'person1':{"name":"bob","age":26},
    'person2':{"name":"david","age":36},
}
print(my_dict['person1']['name'])
print(my_dict['person2']['age'])


print("-----------------------union--------------------")
dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'a':3,'c':4}

merged_dict = dict2|dict1
print(merged_dict)


print("---------# WAP to print common values from two dictionaries-----------")
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 3, 'c': 4}

a = set(dict1.values())
print("The values are:",a)
b = set(dict2.values())
print("The values are:",b)
c = a & b
print("common elements are: ",c)



print("---------------------#create a dictionary and convert keys to sets-------")
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a = set(dict1.keys())
print("The values are:",a)


print("---------------------#create a dictionary and find the unique values-------")
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 10}
a = set(dict1.values())
print("The values are:",a)

# Code to check if a key-value pair exists in a dictionary
print("---------------------# Code to find if a pair exists in the dictionary or not-------")

# Dictionaries
my_dict = {"name": "aman", "age": 22, "Address": "Chandigarh"}
check = {"name", "aman"}

if check in my_dict.items():
    print("exist")
else:
    print("not exist")








