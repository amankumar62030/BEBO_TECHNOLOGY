# 5.	Remove Dictionary Keys That Are in a Set


my_dict = {
    "a":10,
    "b":20,
    "c":30,
    "d":40,
}

to_remove = {"a","c"}

for keys in to_remove:
    if keys in my_dict:
        del my_dict[keys]
print(my_dict)