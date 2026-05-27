'''
Drill 1 — Dunder methods (15 mins)

Create a class called BankAccount with:
- Attributes: owner (str), balance (float)
- __str__  → "BankAccount(owner='Alice', balance=500.0)"
- __repr__ → "BankAccount('Alice', 500.0)"
- __add__  → adds two BankAccount balances, returns a NEW BankAccount
              with the same owner as the left operand
- __eq__   → True if both owner AND balance are equal
- __len__  → returns balance as an integer (int(self.balance))

Example:
a1 = BankAccount("Alice", 500.0)
a2 = BankAccount("Alice", 300.0)
a3 = BankAccount("Bob", 500.0)

str(a1)      → "BankAccount(owner='Alice', balance=500.0)"
repr(a1)     → "BankAccount('Alice', 500.0)"
a1 + a2      → BankAccount("Alice", 800.0)
a1 == a2     → False
a1 == BankAccount("Alice", 500.0) → True
a1 == a3     → False
len(a1)      → 500

'''

class BankAccount:
    def __init__(self,owner:str,balance:float):
        self.owner = owner
        self.balance = balance 
        
    def __repr__(self):
        return f"BankAccount('{self.owner}',{self.balance})"
    
    def __str__(self):
        return f"Bankccount(owner='{self.owner}', balance={self.balance})"
    
    def __add__(self, new_balance):
        if not isinstance(new_balance, BankAccount):
            return NotImplemented
        return BankAccount(self.owner, self.balance + new_balance.balance)
    
    def __eq__(self, new_balance):
        if  not isinstance(new_balance,BankAccount):
            return False
        
        return self.owner == new_balance.owner and self.balance == new_balance.balance
    
    def __len__(self):
        return int(self.balance)