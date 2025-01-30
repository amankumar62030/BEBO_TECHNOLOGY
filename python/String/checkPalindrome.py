
n = input("Enter the string: ")

# # 1st method

# rev_str = ""

# for i in n:
#     rev_str = i + rev_str

# if rev_str == n:
#     print("palindrome")
# else:
#     print("not palindrome")




# 2nd method
rev = n[::-1]
if(n==rev):
    print("Palindrome")
else:
    print("Not palindrome")