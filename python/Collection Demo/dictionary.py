# dictionary = key:value
# list[] = mutable
# tuple() = immutable
# set{}= mutable/immutable
# dict{} = mutable


# key.........................
# must be unique
# must be immutable types--integer, string, tuple
# invalid keys are ----list and dictionary

# value--------------------------
# can be of any type-integer, string, list and other dictionary


print("------------------Empty Dictionary------------")
my_dict = {}
print(type(my_dict))


print(".............#using list of tuples........................")
# list ---not possible because list is mutable

my_dict = dict([("name","aman"),("age",22),("address","Chandigarh")])
print(my_dict)




print("#.................... with dictionary constructor..........................")
my_dict = dict(name='aman',age=22)
print(my_dict)


print("#accessing the elements.................")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
print(my_dict["name"])
print(my_dict["Address"])

# print(my_dict["dept"])      #key error

print(my_dict.get("name"))
print(my_dict.get("Address"))

print(my_dict.get("dept"))      #None



print("# modifying the dictionary--------------------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
print("Before update:",my_dict)
my_dict["name"] = "Rahul"
my_dict["Address"] = "New York"
my_dict["city"] = "nfrnrbjher"          #add at the last if not exist
print("After update",my_dict)


print("..................Deleting key value pair------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
del my_dict["age"]
print(my_dict)


print("------------------pop()----------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
my_dict["dept"] = 101
print(my_dict)

my_dict.popitem()       #it will remove and return the last inserted pair from the dictionary
print(my_dict)


print("................using clear()---------------------------")
my_dict = {"name":"aman","age":22,"Address": "Chandigarh"}
my_dict.clear()
print(my_dict)






