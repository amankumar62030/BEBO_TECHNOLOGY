# 5.	Create a function that prints a pattern of stars in increasing order up to a given number of rows


def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()
n = int(input("Enter the number: "))
pattern(n)