# series...........................
# n = int(input("Enter the number: "))
#
# first = 0
# second = 1
#
# for i in range(1, n + 1):
#     print(first, end=" ")
#     temp = first + second
#     first = second
#     second = temp


# digit........................
n = int(input("Enter the number: "))

first = 0
second = 1
temp= 0
for i in range(1, n):
    print(first, end=" ")
    temp = first + second
    first = second
    second = temp


