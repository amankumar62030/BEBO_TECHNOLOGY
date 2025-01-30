# 5. Read a CSV file named data.csv and print its contents line by line.


file = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\data.csv",'r')
data = file.readlines()
print(data)
for i in data:
    print(i.strip())
file.close()