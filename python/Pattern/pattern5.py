# Enter the number:5
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end =" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()




























    # n = int(input("Enter the number:"))
    #
    # for i in range(n):
    #     for j in range(n - i):
    #         print(" ", end="")
    #     for j in range(i + 1):
    #         print(" *", end="")
    #     print()