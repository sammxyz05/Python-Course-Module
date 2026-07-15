# Encapsulation

## Why Encapsulation Matters

Your Week 3 Log Analyzer probably lets anyone directly modify data:

```python
parser = LogParser()
parser.log_entries = []  # ❌ Direct modification bypasses validation
parser.error_count = -10  # ❌ Invalid state
```

**Encapsulation hides internal state** and exposes a controlled interface. Users of your class can't accidentally break invariants.

## The Three Access Levels

Python doesn't have true private/protected like Java or C++. Instead, it uses **naming conventions** and **name mangling**.

| Convention | Meaning | Example |
|---|---|---|
| `name` | **Public** — part of the public API, use freely | `account.balance` |
| `_name` | **Protected** — internal use, but not enforced | `account._transaction_log` |
| `__name` | **Private** — name-mangled, hard to access from outside | `account.__secret_key` |

## Public Attributes

**Public attributes** are part of your class's API. Users are expected to read and write them.

```python
class Book:
    def __init__(self, title, author):
        self.title = title  # Public
        self.author = author  # Public

book = Book("1984", "Orwell")
print(book.title)  # 1984
book.title = "Animal Farm"  # Allowed
```

**When to use:**
- Simple data that doesn't need validation
- Attributes that are part of the public interface

## Protected Attributes (Single Underscore)

**Protected attributes** are **internal implementation details**. The `_` prefix is a convention that says: "Don't touch this unless you know what you're doing."

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public
        self._balance = balance  # Protected — internal use
        self._transaction_log = []  # Protected
    
    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transaction_log.append(f"Deposit: {amount}")
    
    def get_balance(self):
        """Get current balance."""
        return self._balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # 1500

# You CAN still access protected attributes, but you shouldn't
print(account._balance)  # 1500 — works, but violates convention
```

**When to use:**
- Internal state that shouldn't be modified directly
- Helper attributes that subclasses might need

**Why not enforce it?** Python's philosophy: "We're all consenting adults here." The `_` prefix is a signal, not a lock. If someone needs to access internal state for testing or debugging, they can—but they know they're off the public API.

## Private Attributes (Double Underscore)

**Private attributes** are **name-mangled** to make them harder to access. The `__` prefix triggers Python to rename the attribute to `_ClassName__attribute`.

```python
class SecureAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private — name-mangled
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = SecureAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # 1500

# Direct access fails
# print(account.__balance)  # AttributeError: 'SecureAccount' object has no attribute '__balance'

# But name mangling means it's still accessible if you know the trick
print(account._SecureAccount__balance)  # 1500 — still accessible, but you have to try hard
```

**When to use:**
- Attributes that subclasses should NOT override (rare)
- Sensitive data that you want to protect from accidental access

**When NOT to use:**
- Most of the time. `_protected` is usually sufficient.
- Don't use `__private` just to "hide" things—Python isn't Java. Use it when you genuinely need to prevent subclass name conflicts.

## Name Mangling Explained

Name mangling prevents subclass name conflicts:

```python
class Animal:
    def __init__(self):
        self.__sound = "generic sound"  # Private
    
    def make_sound(self):
        print(self.__sound)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__sound = "bark"  # Different attribute — doesn't overwrite parent's __sound
    
    def bark(self):
        print(self.__sound)

dog = Dog()
dog.make_sound()  # generic sound (parent's __sound)
dog.bark()        # bark (child's __sound)
```

Without name mangling, `Dog.__sound` would overwrite `Animal.__sound`. With mangling:
- `Animal.__sound` becomes `_Animal__sound`
- `Dog.__sound` becomes `_Dog__sound`

They're separate attributes.

## Getters and Setters with `@property`

In Java, you write getters and setters by hand:

```python
# ❌ Java-style — don't do this in Python
class BankAccount:
    def __init__(self, owner, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance

# Usage is clunky
account = BankAccount("Alice", 1000)
account.set_balance(1500)
print(account.get_balance())
```

Python has `@property` for Pythonic getters/setters:

```python
# ✅ Pythonic — use @property
class BankAccount:
    def __init__(self, owner, balance):
        self._balance = balance
    
    @property
    def balance(self):
        """Get balance."""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Set balance with validation."""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

# Usage looks like attribute access
account = BankAccount("Alice", 1000)
account.balance = 1500  # Calls setter
print(account.balance)  # Calls getter
```

**When to use `@property`:**
- You need to validate values before setting
- You need to compute a value on-the-fly (don't store it)
- You want to add getters/setters to an existing attribute without breaking code

**Example — computed property:**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """Compute area on-the-fly."""
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area)  # 50 — computed, not stored
rect.width = 20
print(rect.area)  # 200 — automatically updated
```

## Read-Only Properties

Use `@property` without a setter for read-only attributes:

```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def full_name(self):
        """Read-only computed property."""
        return f"{self._first_name} {self._last_name}"

person = Person("Alice", "Smith")
print(person.full_name)  # Alice Smith

# person.full_name = "Bob Jones"  # AttributeError: can't set attribute
```

## When to Use Each Level

| Use Case | Access Level | Example |
|---|---|---|
| Public API — users should access directly | Public (`name`) | `user.name`, `rect.width` |
| Internal state — subclasses might use | Protected (`_name`) | `self._balance`, `self._cache` |
| Prevent subclass name conflicts | Private (`__name`) | `self.__secret_key` (rare) |
| Validated access | `@property` | `@property def balance(self)` |

**Default to public.** Only hide things when you have a reason:
- Need validation → `@property`
- Internal implementation detail → `_protected`
- Prevent subclass conflict → `__private` (rare)

## Mapping to Projects

**Project 5 (RPG Arena):**
```python
class Character:
    def __init__(self, name, health):
        self.name = name  # Public
        self._health = health  # Protected — validated via methods
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value
```

**Project 6 (IMS):**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price  # Protected — use @property for validation
        self._quantity = quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```

## Key Takeaways

- **Public attributes** (`name`) are part of the public API
- **Protected attributes** (`_name`) are internal, but not enforced—just a convention
- **Private attributes** (`__name`) are name-mangled to prevent subclass conflicts
- **Use `@property`** for validated or computed attributes that look like simple attributes
- **Default to public** unless you have a reason to hide
- **Python trusts you** to respect naming conventions—`_protected` is a signal, not a lock

Next: [Inheritance](./03-inheritance.md)
