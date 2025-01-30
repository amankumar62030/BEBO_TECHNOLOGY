
s1 = input("Enter the String: ")
rev_str = ""
for i in s1:
    rev_str = i + rev_str

if s1 == rev_str:
    print(f"{s1} is Palindrome")
else:
    print(f"{s1} is not Palindrome")


print("---------------------------------2nd Method---------------------")
# rev_str = s1[::-1]
# if(s1 == rev_str):
#     print(f"{s1} is Palindrome")
# else:
#     print(f"{s1} is not Palindrome")