# Define a custom exception class called InsufficientBalance Exception. Write a program
# where the user tries to withdraw an amount from their bank balance. Raise this exception if the
# withdrawal amount exceeds the balance.

class InsufficientBalance(Exception):
    def __init__(self,message="Insufficient balance for the transaction"):
        super().__init__(message)

def withdraw(balance,amount):
    if amount>balance:
        raise InsufficientBalance
    balance-=amount
    print(f"Remaining balance : {balance}")
    return balance

try:
    balance = float(input("Enter your bank balance: "))
    amount = float(input("Enter the amount to withdraw: "))
    balance = withdraw(balance, amount)

except InsufficientBalance as e:
    print(f"Error: {e}")
except ValueError:
    print("Error:Please enter valid numeric value")

