# Write a Python function that checks whether a given key exists in a dictionary. If the key is present, return its value; otherwise, return 'Key not found'.

def check_key_exists(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return 'Key not found'
dict1 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 10,
}
key_to_check = input("Enter the key to check: ")
result = check_key_exists(dict1, key_to_check)
print(result)
