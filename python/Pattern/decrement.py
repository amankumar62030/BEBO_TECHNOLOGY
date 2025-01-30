# Enter the number: 5
# * * * * *
# * * * *
# * * *
# * *
# *


n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(i,n+1):
        print("7 ",end="")
    print()
