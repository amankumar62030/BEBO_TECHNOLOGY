# 7.	Create a function to check whether a given string is a palindrome.

def is_palindrome(num):
    rev = ""
    for i in num:
        rev=i+rev
    if num!=rev:
        print("Not Palindrome")
    else:
        print("Palindrome")

num = input("Enter the String: ")
is_palindrome(num)