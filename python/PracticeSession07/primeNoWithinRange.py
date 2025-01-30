# Write a function called prime_numbers that takes two integers start and end and returns a list of all prime numbers within that range (inclusive).


def prime_numbers(r1,r2):
    prime = []
    for i in range(r1,r2+1):
        if i<2:
            continue

        is_prime = True
        if i%2==0:
            is_prime = False
        else:
             prime.append(i)
    print(prime)

r1 = int(input("Enter first number:"))
r2 = int(input("Enter second number: "))
prime_numbers(r1,r2)


