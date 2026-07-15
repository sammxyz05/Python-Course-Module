# Classes, Instances, and Attributes

## Why Classes Matter

Your Week 3 Cart Engine probably looks like this:

```python
cart = []

def add_item(item, price, quantity):
    cart.append({"item": item, "price": price, "quantity": quantity})

def calculate_total(discount=None):
    total = sum(item["price"] * item["quantity"] for item in cart)
    if discount:
        total *= (1 - discount)
    return total
```

This works, but it has problems:
- **Global state:** The `cart` variable is global—hard to test, hard to have multiple carts
- **Loose coupling:** Functions assume `cart` exists and has a specific structure
- **No encapsulation:** Anyone can modify `cart` directly, bypassing your logic

**Classes fix this** by bundling data (attributes) and behavior (methods) together.

## Basic Class Syntax

```python
class BankAccount:
    """A simple bank account."""
    
    def __init__(self, owner, balance=0):
        """Initialize a new account."""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
    
    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

# Create instances (objects)
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob")

# Call methods
alice_account.deposit(500)
print(alice_account.balance)  # 1500

bob_account.deposit(100)
print(bob_account.balance)    # 100
```

**Anatomy:**
- `class BankAccount:` — Define a class (PascalCase by PEP 8)
- `__init__(self, owner, balance=0)` — Constructor method, runs when you create an instance
- `self` — The instance itself (see below)
- `self.owner`, `self.balance` — Instance attributes (each object has its own)
- `deposit`, `withdraw` — Methods (functions that belong to the class)

## Understanding `self`

**`self` is the instance.**

When you call:
```python
alice_account.deposit(500)
```

Python rewrites it to:
```python
BankAccount.deposit(alice_account, 500)
```

**`self` is how a method knows which instance it's operating on.** When `deposit` says `self.balance += amount`, it's modifying **that specific instance's** balance.

**Why the name `self`?** It's a convention. You could call it `this` or `me` or `obj`, but **don't**—every Python programmer expects `self`.

**Why is it explicit?** Other languages (Java, JavaScript) hide `this`, which causes confusion. Python makes it explicit: if you see `self.x`, you know it's an instance attribute. If you see `x`, you know it's a local variable.

## Instance Attributes

Instance attributes are **per-object**. Each instance has its own copy.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)

print(buddy.name)  # Buddy
print(max_dog.name)  # Max
```

**Defining instance attributes:**
- Always define them in `__init__` (or another method)
- Always use `self.attribute_name`
- You can add attributes later, but it's bad practice—define everything in `__init__` so readers know what the class has

**Reading and writing:**
```python
buddy.age = 6  # Update attribute
print(buddy.age)  # 6
```

## Class Attributes

Class attributes are **shared across all instances**. They belong to the class, not any one object.

```python
class Dog:
    # Class attribute — shared by all dogs
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes — unique to each dog
        self.name = name
        self.age = age

buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)

print(buddy.species)  # Canis familiaris
print(max_dog.species)  # Canis familiaris

# All instances see the same class attribute
Dog.species = "Canis lupus familiaris"
print(buddy.species)  # Canis lupus familiaris
print(max_dog.species)  # Canis lupus familiaris
```

**When to use class attributes:**
- Constants shared by all instances (`PI = 3.14159`)
- Default values (`DEFAULT_TIMEOUT = 30`)
- Counters (`instance_count` to track how many instances were created)

**Trap — mutable class attributes:**
```python
class Cart:
    items = []  # ❌ WRONG: shared across all instances!
    
    def add_item(self, item):
        self.items.append(item)

cart1 = Cart()
cart2 = Cart()

cart1.add_item("apple")
print(cart2.items)  # ['apple'] — SURPRISE! Both carts share the same list

# ✅ CORRECT: use instance attributes for mutable data
class Cart:
    def __init__(self):
        self.items = []  # Each cart gets its own list
```

## Methods vs Functions

A **method** is a function defined inside a class. The first parameter is always `self` (the instance).

```python
class Calculator:
    def add(self, a, b):
        """A method — belongs to the class."""
        return a + b

calc = Calculator()
print(calc.add(10, 20))  # 30
```

Methods can access instance attributes and call other methods:

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self):
        """Return full name."""
        return f"{self.first_name} {self.last_name}"
    
    def greet(self):
        """Greet the person."""
        return f"Hello, {self.get_full_name()}!"

person = Person("Alice", "Smith")
print(person.greet())  # Hello, Alice Smith!
```

## Constructor Pattern: `__init__`

**`__init__` is not a constructor—it's an initializer.** Python creates the object first, then calls `__init__` to set it up.

**Best practices:**
- Initialize all instance attributes in `__init__`
- Use default parameter values for optional configuration
- Call validation logic if needed

```python
class Rectangle:
    def __init__(self, width, height):
        """Initialize a rectangle."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area."""
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area())  # 50
```

## Mapping to Week 3 Concepts

Think of classes as **namespaces that group related functions and data**:

| Week 3 (procedural) | Week 4 (OOP) |
|---|---|
| `cart = []` (global) | `self.items = []` (instance attribute) |
| `def add_item(cart, item)` | `def add_item(self, item)` |
| `calculate_total(cart)` | `self.calculate_total()` |
| Multiple functions + global state | One class with methods + instance state |

**When to use classes vs functions:**
- **Functions:** Stateless transformations (`calculate_tax(amount)`, `validate_email(email)`)
- **Classes:** Stateful objects that group related data and behavior (`BankAccount`, `ShoppingCart`, `User`)

## Mapping to Projects

**Project 5 (RPG Arena):**
- `Character` class with `name`, `health`, `attack_power` attributes
- `attack()` method that reduces another character's health
- Subclasses: `Warrior`, `Mage`, `Archer` with different abilities

**Project 6 (IMS):**
- `Product` class with `name`, `price`, `quantity` attributes
- `Inventory` class with a list of products and methods to add/remove/search
- `Invoice` class to calculate totals with discounts and taxes

## Key Takeaways

- **Classes bundle data (attributes) and behavior (methods)** into reusable blueprints
- **Instances are objects** created from a class: `obj = MyClass()`
- **`__init__` initializes instances** when they're created
- **`self` is the instance** — the first parameter of every method
- **Instance attributes** (`self.x`) are per-object, unique to each instance
- **Class attributes** (`ClassName.x`) are shared across all instances
- **Methods access attributes** and other methods via `self`
- **Use classes for stateful objects**, functions for stateless transformations

Next: [Encapsulation](./02-encapsulation.md)
