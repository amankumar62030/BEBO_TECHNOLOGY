# Calculate Power: Write a function that takes two integers, base and exponent, and calculates the power of base raised to exponent using a loop. Do not use Pythonâ€™s built-in power function.

# base = int(input("Enter the base:"))
# power = int(input("Enter the Power"))
#
# result = 1
#
# for i in range(power):
#     result*=base
# print(result)
#
#
#
# print(5**2)


base = int(input("Base"))
power = int(input("Power"))
result = 1
for i in range(power):
    result*=base
print(result)

print(base**power)