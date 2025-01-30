# Write a program to simulate a login system. It should check if:
# •	The entered username matches the stored username and
# •	The entered password matches the stored password.

username = "aman123"
password = 12345
n = input("Enter the username: ")
p = int(input("Enter the password: "))

if(username == n ):
    print("The username matches successfully!")
else:
    print("The username doesnot matches")

if(password == p):
    print("the password matches successfully!")
else:
    print("The passowrd does not matches")
