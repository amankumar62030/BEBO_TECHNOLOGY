#Reading of the file from text

file = open(r"D:\BEBO TECHNOLOGY\python\File Handling\readFile.txt")
data =file.read()
print(data)
print(file.readline())      #only print first line
print(file.readable())
print(file.writable())
file.close()


