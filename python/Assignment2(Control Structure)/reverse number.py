# Reverse a Number: Write a program that takes an integer as input and outputs the reverse of that number.

# n = int(input("Enter the number: "))
# rev_no = 0
# while n!=0:
#     rem = n%10
#     rev_no = rev_no*10 + rem
#     n=n//10
# print(rev_no)

def reverse_no(n):
    rev_no = 0
    while n>0:
        rem = n%10
        rev_no = rev_no*10+rem
        n//=10
    return rev_no

n = int(input("Enter the number: "))
s=reverse_no(n)
print(s)