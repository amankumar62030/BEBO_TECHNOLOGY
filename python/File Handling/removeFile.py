import os
try:
    os.remove(r"D:\BEBO TECHNOLOGY\python\File Handling\removeFile.txt")
    print("THe file is deleted")
except FileNotFoundError as e:
    print(e)



# for directory
try:
    os.rmdir(r"D:\BEBO TECHNOLOGY\python\File Handling\remDir")
    print("THe file is deleted")
except FileNotFoundError as e:
    print(e)
