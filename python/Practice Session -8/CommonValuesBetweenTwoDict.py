# 1.	Find Common Values Between Two Dictionaries Using Sets

my_dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}
my_dict2 = {
    "a": 10,
    "b": 4,
    "c": 20
}

a = set(my_dict1.values())
b = set(my_dict2.values())

common = a & b
print(common)


