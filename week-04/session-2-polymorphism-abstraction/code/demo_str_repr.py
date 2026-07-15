"""
Demo: __str__ vs __repr__
Shows: the difference between __str__ and __repr__, when to use each
"""

# Basic difference
print("=== Basic Difference ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """For end users — readable."""
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        """For developers — unambiguous, ideally eval()-able."""
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)

print("str(person):", str(person))      # Calls __str__
print("repr(person):", repr(person))    # Calls __repr__
print("print(person):", person)         # Calls __str__ by default

# In a container, repr is used
print("\nIn a list:", [person])         # Uses __repr__


# Only __repr__ defined
print("\n=== Only __repr__ Defined ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "Orwell")
print("str(book):", str(book))    # Falls back to __repr__
print("repr(book):", repr(book))  # Uses __repr__


# Only __str__ defined (not recommended)
print("\n=== Only __str__ Defined (not recommended) ===")

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f'"{self.title}" ({self.year})'

movie = Movie("Inception", 2010)
print("str(movie):", str(movie))   # Uses __str__
print("repr(movie):", repr(movie)) # Falls back to default (ugly)


# eval()-able __repr__
print("\n=== eval()-able __repr__ ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Can be eval()-ed to recreate the object."""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """User-friendly format."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        """For comparison after eval."""
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
print("Original point:", p1)
print("repr:", repr(p1))

# You can eval() the repr to recreate the object
p2 = eval(repr(p1))
print("Eval'd point:", p2)
print("Are they equal?", p1 == p2)


# When __repr__ is not eval()-able (common in practice)
print("\n=== Non-eval()-able __repr__ (still useful) ===")

class User:
    def __init__(self, username, email, created_at):
        self.username = username
        self.email = email
        self.created_at = created_at

    def __str__(self):
        """For end users."""
        return f"{self.username} ({self.email})"

    def __repr__(self):
        """For developers — shows all important state."""
        return f"User(username='{self.username}', email='{self.email}', created_at='{self.created_at}')"

user = User("alice", "alice@example.com", "2024-01-01")
print("str(user):", str(user))
print("repr(user):", repr(user))


# Debugging with __repr__
print("\n=== Debugging with __repr__ ===")

class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        """Helpful for debugging."""
        return f"Transaction(amount=${self.amount:.2f}, description='{self.description}')"

transactions = [
    Transaction(100.50, "Groceries"),
    Transaction(50.00, "Gas"),
    Transaction(1200.00, "Rent")
]

print("Transactions list:")
print(transactions)  # Uses __repr__ for each item


# String formatting
print("\n=== String Formatting ===")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Product(name='{self.name}', price=${self.price:.2f})"

product = Product("Laptop", 999.99)

# Different ways to format
print(f"Using f-string: {product}")              # Uses __str__
print(f"Using f-string with !r: {product!r}")   # Forces __repr__
print(f"Using f-string with !s: {product!s}")   # Forces __str__


# Best practices
print("\n=== Best Practices ===")

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __str__(self):
        """End-user view — hide account number."""
        return f"{self.owner}'s account: ${self.balance:.2f}"

    def __repr__(self):
        """Developer view — show everything."""
        return f"BankAccount(account_number='{self.account_number}', owner='{self.owner}', balance={self.balance})"

account = BankAccount("123-456-789", "Alice", 5000)

# End user sees friendly version
print("Customer sees:", account)

# Developer sees full details
print("Developer sees:", repr(account))

# In logs/debugging, repr is more useful
import logging
logging.basicConfig(level=logging.INFO)
logging.info(f"Account created: {repr(account)}")


# Summary
print("\n=== Summary ===")
print("""
__str__:
  - For end users
  - Readable, friendly format
  - Called by str(), print(), f"{obj}"
  - If missing, falls back to __repr__

__repr__:
  - For developers
  - Unambiguous, detailed
  - Ideally eval()-able (but not required)
  - Called by repr(), f"{obj!r}", container displays
  - ALWAYS implement this one

Best practice:
  - Always implement __repr__ (for debugging)
  - Implement __str__ only if you need user-friendly output
""")
