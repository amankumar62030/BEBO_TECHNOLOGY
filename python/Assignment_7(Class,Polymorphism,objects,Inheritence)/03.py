# 3.	Write a class Calculator with a method add() that can handle two or three arguments. Use
# default arguments to achieve method overloading behavior.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

result1 = calc.add(5, 10)
print(f"Sum of 5 and 10: {result1}")

result2 = calc.add(5, 10, 15)
print(f"Sum of 5, 10, and 15: {result2}")
