# 7.	Find Common Keys Between a Dictionary and a Set

my_dict = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

my_set = {"b", "d", "e"}

common_keys = my_dict.keys() & my_set

print(common_keys)
