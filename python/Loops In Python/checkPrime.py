
n = int(input("Enter the number: "))
is_prime = True
for i in range(2,n):
    if(n%i==0):
        is_prime  = False
        break

if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# n = int(input("Enter the number: "))
#
# if is_prime(n):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")


