# 4.Check if two strings are anagrams

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1)!=len(str2):
    print("Not anagram")
else:
    a = sorted(str1)
    b = sorted(str2)

    if a == b:
        print("Anagram")
    else:
        print("Not Anagram")