# 1.	Write a Python program that reads a file named data.txt. Use exception handling to manage the following scenarios:
# •	The file does not exist.
# •	The file is empty.
# •	Any unexpected error during file reading.

file = open(r"D:\BEBO TECHNOLOGY\python\Assignment-8(Exception Handling and File Handling)\data.txt")

try:
    data = file.read()
    print(data)
except FileNotFoundError as e:
    print(e)
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")