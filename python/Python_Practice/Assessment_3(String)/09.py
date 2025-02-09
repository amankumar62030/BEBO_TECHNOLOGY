# 9.Write a Python program to remove duplicate characters from a string while preserving the order of characters.

def remove_dup(n):
    str = ""
    for i in n:
        if i not in str:
            str+=i
    return str

n = input("Enter the String: ")
print(remove_dup(n))