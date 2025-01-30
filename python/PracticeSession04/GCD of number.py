
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 > num1:
    num1, num2 = num2, num1

while num2 != 0:
    remainder = num1 % num2      #15%12=3         12%3=4
    num1 = num2     #num1=12      num1=3
    num2 = remainder  #num2 = 3       num2=4

print("The GCD of the numbers is:", num1)



