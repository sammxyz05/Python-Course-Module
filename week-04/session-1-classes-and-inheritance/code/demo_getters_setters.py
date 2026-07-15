"""
Demo: Getters and Setters with @property
Shows: Pythonic property decorators for controlled attribute access
"""

class BankAccount:
    """Bank account with validated balance using @property."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Protected — accessed via property

    @property
    def balance(self):
        """Get balance (getter)."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Set balance with validation (setter)."""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount  # Uses setter for validation


# Usage looks like attribute access
print("=== Using @property ===")
account = BankAccount("Alice", 1000)

# Getter
print(f"Balance: ${account.balance}")

# Setter with validation
account.balance = 1500
print(f"Updated balance: ${account.balance}")

# Setter catches invalid values
try:
    account.balance = -100
except ValueError as e:
    print(f"Error: {e}")

# Deposit uses setter internally
account.deposit(500)
print(f"After deposit: ${account.balance}")


# Read-only property (no setter)
print("\n=== Read-only property ===")

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        """Read-only computed property."""
        return f"{self._first_name} {self._last_name}"

    @property
    def initials(self):
        """Another read-only computed property."""
        return f"{self._first_name[0]}.{self._last_name[0]}."


person = Person("Alice", "Smith")
print(f"Full name: {person.full_name}")
print(f"Initials: {person.initials}")

# Can't set read-only property
try:
    person.full_name = "Bob Jones"
except AttributeError as e:
    print(f"Error: {e}")


# Computed property (not stored)
print("\n=== Computed property ===")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """Compute area on-the-fly."""
        return self.width * self.height

    @property
    def perimeter(self):
        """Compute perimeter on-the-fly."""
        return 2 * (self.width + self.height)


rect = Rectangle(5, 10)
print(f"Area: {rect.area}")         # 50 — computed, not stored
print(f"Perimeter: {rect.perimeter}")  # 30

# Area updates automatically when dimensions change
rect.width = 20
print(f"New area: {rect.area}")     # 200 — automatically updated


# Lazy property (computed once, then cached)
print("\n=== Lazy property (cached) ===")

class ExpensiveCalculation:
    def __init__(self, n):
        self.n = n
        self._result = None  # Cache

    @property
    def result(self):
        """Compute once, then cache."""
        if self._result is None:
            print(f"Computing expensive result for {self.n}...")
            self._result = sum(range(self.n))
        return self._result


calc = ExpensiveCalculation(1000000)
print(f"Result: {calc.result}")  # Computes
print(f"Result: {calc.result}")  # Returns cached value (no computation)
