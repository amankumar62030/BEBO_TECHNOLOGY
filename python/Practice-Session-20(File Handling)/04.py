# 4. Write a Python program to count the number of words in a file called document.txt.


file = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\document.txt")
content = file.read()
print(content)
num = content.split()
print(num)
print("The length is: ",len(num))
file.close()