"""
Demo: Encapsulation
Shows: public, protected (_), and private (__) attributes
"""

class BankAccount:
    """Demonstrates three levels of access."""

    def __init__(self, owner, balance, account_number):
        self.owner = owner                    # Public
        self._balance = balance               # Protected
        self.__account_number = account_number  # Private (name-mangled)

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")

    def get_balance(self):
        """Get current balance (controlled access)."""
        return self._balance

    def _internal_audit(self):
        """Protected method — internal use."""
        print(f"Audit: Account {self.__account_number}, Balance: ${self._balance}")

    def __validate_transaction(self, amount):
        """Private method — name-mangled."""
        return amount > 0 and amount <= self._balance


# Create account
account = BankAccount("Alice", 1000, "123-456-789")

# Public access — works fine
print("=== Public access ===")
print(f"Owner: {account.owner}")
account.owner = "Alice Smith"
print(f"Updated owner: {account.owner}")

# Protected access — works, but violates convention
print("\n=== Protected access (discouraged) ===")
print(f"Balance: {account._balance}")  # Works, but you shouldn't do this
account._balance = 5000  # Works, but bypasses validation!
print(f"Modified balance: {account._balance}")

# Use the public interface instead
account = BankAccount("Bob", 500, "987-654-321")
print(f"\nBalance via public method: {account.get_balance()}")

# Private access — fails
print("\n=== Private access (name-mangled) ===")
try:
    print(account.__account_number)
except AttributeError as e:
    print(f"Error: {e}")

# But name mangling means it's still accessible if you know the trick
print(f"Accessing via name mangling: {account._BankAccount__account_number}")

# Protected method — works, but discouraged
print("\n=== Protected method ===")
account._internal_audit()  # Works, but signals "internal use"

# Demonstrating inheritance with private attributes
print("\n=== Name mangling prevents subclass conflicts ===")

class Animal:
    def __init__(self):
        self.__sound = "generic sound"  # Private

    def make_sound(self):
        print(f"Animal sound: {self.__sound}")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__sound = "bark"  # Different attribute — doesn't overwrite parent's

    def bark(self):
        print(f"Dog sound: {self.__sound}")

dog = Dog()
dog.make_sound()  # generic sound (parent's __sound)
dog.bark()        # bark (child's __sound)

# Both __sound attributes exist, name-mangled differently
print(f"Parent's sound: {dog._Animal__sound}")
print(f"Child's sound: {dog._Dog__sound}")
