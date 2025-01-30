# 4.	Check if a Set of Keys Exists in a Dictionary


my_dict = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

check = {"a", "c"}
if check.issubset(my_dict.keys()):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
