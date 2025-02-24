# Sum of Digits Until Single Digit: Create a function that takes an integer as input and repeatedly finds the sum of its digits until a single-digit number is obtained. For example,
# if the input is 9875, the output should be 2 (9+8+7+5=29 -> 2+9=11 -> 1+1=2).
# sum of digits until single digit--------------------------------------------------------
def sum_of_digit(n):
    while n>10:
        sum = 0
        while n>0:
            rem = n%10
            sum+=rem
            n//=10
        n = sum
    return n
n = int(input("Enter the number :"))
s = sum_of_digit(n)
print(s)