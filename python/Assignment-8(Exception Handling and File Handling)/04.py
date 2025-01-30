# 4.	Write a script to read lines from a file records.txt and print them to the console.
# Add exception handling to manage file not found and permission errors.

try:
    file = open(r"D:\BEBO TECHNOLOGY\python\Assignment-8(Exception Handling and File Handling)\records.txt")
    print(file.read())
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)