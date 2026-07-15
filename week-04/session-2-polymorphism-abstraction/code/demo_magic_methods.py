"""
Demo: Magic Methods Overview
Shows: common magic methods and their usage
"""

# String representation
print("=== String Representation ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """User-friendly representation."""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """Developer representation."""
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "George Orwell")
print(f"str(book): {str(book)}")
print(f"repr(book): {repr(book)}")
print(f"print(book): {book}")


# Comparison methods
print("\n=== Comparison Methods ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """Equal if same age."""
        return self.age == other.age

    def __lt__(self, other):
        """Less than if younger."""
        return self.age < other.age

    def __str__(self):
        return f"{self.name} ({self.age})"

alice = Person("Alice", 30)
bob = Person("Bob", 25)
charlie = Person("Charlie", 30)

print(f"{alice} == {bob}: {alice == bob}")
print(f"{alice} == {charlie}: {alice == charlie}")
print(f"{bob} < {alice}: {bob < alice}")
print(f"{alice} > {bob}: {alice > bob}")

# Sorting uses __lt__
people = [alice, bob, charlie]
sorted_people = sorted(people)
print(f"Sorted by age: {[str(p) for p in sorted_people]}")


# Arithmetic methods
print("\n=== Arithmetic Methods ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply by scalar")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"{v1} + {v2} = {v1 + v2}")
print(f"{v2} - {v1} = {v2 - v1}")
print(f"{v1} * 3 = {v1 * 3}")


# Container methods
print("\n=== Container Methods ===")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        """Return number of items."""
        return len(self.items)

    def __getitem__(self, index):
        """Get item by index."""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set item by index."""
        self.items[index] = value

    def __contains__(self, item):
        """Check if item is in cart."""
        return item in self.items

    def __iter__(self):
        """Make cart iterable."""
        return iter(self.items)

cart = ShoppingCart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("orange")

print(f"Cart length: {len(cart)}")
print(f"First item: {cart[0]}")
print(f"'apple' in cart: {'apple' in cart}")
print(f"'grape' in cart: {'grape' in cart}")

# Iterate over cart
print("Items in cart:")
for item in cart:
    print(f"  - {item}")

# Indexing and slicing
cart[1] = "mango"
print(f"After replacing banana: {list(cart)}")


# Callable objects
print("\n=== Callable Objects ===")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Make object callable."""
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")


# Context manager
print("\n=== Context Manager ===")

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        return False  # Don't suppress exceptions

# Usage (creates a temporary file)
import tempfile
import os

temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
temp_path = temp_file.name
temp_file.close()

try:
    with ManagedFile(temp_path) as f:
        f.write("Hello, World!")
    print("File written successfully")
finally:
    os.unlink(temp_path)


# Rich comparison example
print("\n=== Rich Comparison Example ===")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius

    def __str__(self):
        return f"{self.celsius}°C"

t1 = Temperature(20)
t2 = Temperature(25)
t3 = Temperature(20)

print(f"{t1} == {t3}: {t1 == t3}")
print(f"{t1} < {t2}: {t1 < t2}")
print(f"{t2} > {t1}: {t2 > t1}")
print(f"{t1} <= {t3}: {t1 <= t3}")


# Complete example with multiple magic methods
print("\n=== Complete Example: BankAccount ===")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __eq__(self, other):
        """Accounts are equal if same balance."""
        return self.balance == other.balance

    def __lt__(self, other):
        """Compare by balance."""
        return self.balance < other.balance

    def __add__(self, amount):
        """Add money (deposit)."""
        return BankAccount(self.owner, self.balance + amount)

    def __sub__(self, amount):
        """Subtract money (withdraw)."""
        return BankAccount(self.owner, self.balance - amount)

    def __len__(self):
        """Return balance as integer (for fun)."""
        return int(self.balance)

account = BankAccount("Alice", 1000)
print(account)
print(repr(account))

new_account = account + 500  # Deposit
print(f"After deposit: {new_account}")

new_account = new_account - 200  # Withdraw
print(f"After withdrawal: {new_account}")

print(f"Balance as int: {len(new_account)}")
