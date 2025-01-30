# 8. Write a program to merge the contents of two files, filel.txt and file2.txt, into a new file called
# merged.txt.

f1 =open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\file1.txt")
f2 =open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\file2.txt")
f3 =open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\mergefile.txt","w")

first = f1.read()
second = f2.read()
merge = first +" "+ second
f3.write(merge)
print("Merging successfully done.........")
f1.close()
f2.close()
f3.close()