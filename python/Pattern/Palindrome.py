n = int(input("Enter any number: "))

t = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if t == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
