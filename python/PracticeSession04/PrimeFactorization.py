
num = int(input("Enter the number:"))
factor = 2

while num > 0:
    while num % factor == 0:
        print(factor,end=" ")
        num//=factor
    factor+=1
print()