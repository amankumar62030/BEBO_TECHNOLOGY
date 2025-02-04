# 1.Check if a string is a palindrome.

my_str = input("Enter the String: ")

rev_str = ""
for i in my_str:
    rev_str = i+rev_str

if rev_str == my_str:
    print("Palindrome")
else:
    print("Not Palindrome")