# 1. Write a Python script to create a file called example.txt, write the text "Python programming is interesting" into it, and close the file.

st = "Python programming is interesting"
file = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\example.txt",'w')
data = file.write(st)
print("Write done...........")
file.close()
