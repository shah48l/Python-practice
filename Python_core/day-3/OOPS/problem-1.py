'''
Problem 1
Create a class called BankAccount with:
- Attributes: owner (str), balance (float)
- A method deposit(amount) that adds to balance
- A method withdraw(amount) that subtracts from balance
  but prints "Insufficient funds" if balance goes below 0
- A __str__ that returns:
  "Account[owner=Shahid, balance=500.0]"

Example:
acc = BankAccount("Shahid", 500.0)
acc.deposit(200)
acc.withdraw(100)
print(acc) → "Account[owner=Shahid, balance=600.0]"

'''

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            print(f"Amount withdrawn {amount}. New balance {self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[owner={self.owner}, balance={self.balance}]"


my_account = BankAccount("Alice", 100)

my_account.deposit(50)
my_account.withdraw(30)

print(my_account)