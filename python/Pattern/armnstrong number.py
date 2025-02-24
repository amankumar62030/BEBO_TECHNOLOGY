# armnstrong number----------------------------------

n = int(input("Enter the number: "))

len_n = len(str(n))
copy_n = n
sum = 0
while n > 0:
    rem = n % 10
    sum += rem ** len_n
    n //= 10

if copy_n == sum:
    print("Armnstrong number")
else:
    print("Not a Armnstrong number")
