# 5.	Create a parent class BankAccount with a method deposit(). Create two child classes,
# SavingsAccount and CurrentAccount, that override the deposit() method to include specific rules
# for each account type.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount < 100:
            print("Deposit amount must be at least 100 for Savings Account.")
        else:
            super().deposit(amount)

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        fee = 5
        amount_after_fee = amount - fee
        if amount_after_fee < 0:
            print("Deposit amount is too small after fee. Please deposit more.")
        else:
            self.balance += amount_after_fee
            print(f"Deposited {amount} (after fee of {fee}). New balance: {self.balance}")

savings_account = SavingsAccount(1000)
savings_account.deposit(50)
savings_account.deposit(200)

current_account = CurrentAccount(500)
current_account.deposit(50)
current_account.deposit(100)
