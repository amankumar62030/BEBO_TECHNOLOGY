# Write a program that demonstrates the use of identity operators (is, is not).
# 1.	Define two variables, a and b, and assign them the same integer value.
# 2.	Use is and is not to check if a and b reference the same object in memory.
# 3.	Print the results of each comparison.

a = 10
b = 10
print(a is b)
print(a is not b)

c = 34
d = c
print(c is d)
print(c is not d)