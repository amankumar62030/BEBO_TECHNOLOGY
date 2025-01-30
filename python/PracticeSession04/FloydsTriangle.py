
n = int(input("Enter the number:"))
count = 1
for i in range(n):
    for j in range( n -i):
        print(" " ,end=" ")
    for j in range( i +1):
        print(count ," " ,end=" ")
        count+=1
    print()


