# 9.	Create a class BankAccount with methods to deposit, withdraw, and check balance

class BankAccount:
    def __init__(self,initial_balance=0):
        self.balance = initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited successfully. New Balance is : {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"{amount} withdraw successfully. Remaining balance: {self.balance}")
        elif amount>self.balance:
            print("Insufficient funds")
        else:
            print("Invalid withdrawal amount")

    def check_balance(self):
        print(f"Current balance is : {self.balance}")
account = BankAccount(500)
account.deposit(200)
account.withdraw(100)
account.check_balance()