# Create a class BankAccount with method to deposit, withdraw and check balance

class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0.0

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw amount {amount}")
    def check_balance(self):
           print(f"Account balance: {self.balance}")

account = BankAccount("Aman Kumar")
account.check_balance()
account.deposit(200000)
account.withdraw(150000)
account.check_balance()