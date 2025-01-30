# 9.	Create two classes, EvenNumbers and OddNumbers, with a method generate_numbers(n) that generates
# the first n even or odd numbers. Write a function that takes an object of either class and prints the
# numbers.

class EvenNumbers:
    def generate_numbers(self, n):
        i = 0
        count = 0
        while count < n:
            if i % 2 == 0:
                print(i, end=" ")
                count += 1
            i += 1
        print()

class OddNumbers:
    def generate_numbers(self, n):
        i = 1
        count = 0
        while count < n:
            if i % 2 != 0:
                print(i, end=" ")
                count += 1
            i += 1
        print()

def print_numbers(number_generator, n):
    number_generator.generate_numbers(n)

even_generator = EvenNumbers()
odd_generator = OddNumbers()

print("First 5 even numbers:")
print_numbers(even_generator, 5)

print("First 5 odd numbers:")
print_numbers(odd_generator, 5)
