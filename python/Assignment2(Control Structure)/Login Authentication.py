# Login Authentication: Write a program that accepts a username and password from the user and checks if they match the pre-set username and password. If both match, print "Access Granted"; otherwise, print "Access Denied."

_username = "aman321"
_password = "1234"

username = input("Enter the username: ")
password = input("Enter the password: ")

if(username == _username and password == _password):
    print("Access Granted")
else:
    print("Access Denied")