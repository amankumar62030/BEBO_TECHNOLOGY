# Write a Python function that finds all keys in a dictionary that have a specific value

def find_keys_by_value(dictionary, target_value):
    result = []
    for key in dictionary:
        if dictionary[key] == target_value:
            result.append(key)
    return result

dict1 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
}

value_to_find = int(input("Enter the value to find keys for: "))
keys = find_keys_by_value(dict1, value_to_find)

if keys:
    print(f"Keys with value {value_to_find}: {keys}")
else:
    print(f"No keys found with value {value_to_find}.")
