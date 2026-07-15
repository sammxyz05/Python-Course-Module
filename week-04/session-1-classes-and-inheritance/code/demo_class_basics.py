"""
Demo: Class Basics
Shows: class definition, __init__, self, instance attributes, methods
"""

class BankAccount:
    """A simple bank account."""

    def __init__(self, owner, balance=0):
        """Initialize a new account."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Balance: ${self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        """Return current balance."""
        return self.balance


# Create instances
print("=== Creating accounts ===")
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob")  # Uses default balance of 0

print(f"{alice_account.owner}'s balance: ${alice_account.balance}")
print(f"{bob_account.owner}'s balance: ${bob_account.balance}")

# Use methods
print("\n=== Transactions ===")
alice_account.deposit(500)
alice_account.withdraw(200)
alice_account.withdraw(2000)  # Insufficient funds

bob_account.deposit(100)
bob_account.withdraw(50)

print(f"\n=== Final balances ===")
print(f"{alice_account.owner}: ${alice_account.get_balance()}")
print(f"{bob_account.owner}: ${bob_account.get_balance()}")
