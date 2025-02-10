# 12.Write a Python function that finds all keys in a dictionary that have a specific value


dict1 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

target_value = int(input("Enter the target value: "))

keys =[]
for key,value in dict1.items():
    if value==target_value:
        keys.append(key)
if keys:
    print(f"Keys found: {keys}")
else:
    print("No keys found")

