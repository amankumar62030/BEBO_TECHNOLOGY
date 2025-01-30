# 6. Write a program to copy the contents of a file source,txt to another file destination.txt.


f1 = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\source.txt",'r')
f2 = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\destination.txt",'w')

data = f1.read()
f2.write(data)
f1.close()
f2.close()
