# 10.Write a Python function that checks whether a given key exists in a dictionary. If the key is present, return its value; otherwise, return 'Key not found'.

dict1 = {
    "1":"aman",
    "2":"anshu",
    "3":"Rohit"
}

keys_to_search = input("Enter the key to search: ")

if keys_to_search in dict1:
    print(dict1[keys_to_search])
else:
    print("Keys not found")
