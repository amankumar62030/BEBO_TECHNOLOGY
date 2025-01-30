# 2. Write a program to read and display the contents of a file named example.txt.

file = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\example.txt",'r')
data = file.read()
print(data)
file.close()

