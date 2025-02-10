# 6.Write a Python program that reverses the order of words in a given sentence.

def reverse_str(str1):
    words = str1.split()
    reverse = [word[::-1] for word in words]
    reversed_string = ' '.join(reverse)
    return reversed_string

str1 = input("Enter the string: ")
print(reverse_str(str1))