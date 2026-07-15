# Magic Methods (Dunder Methods)

## What Are Magic Methods

**Magic methods** (also called **dunder methods** for "double underscore") are special methods that Python calls automatically when you use built-in syntax:

- `print(obj)` → calls `obj.__str__()`
- `len(obj)` → calls `obj.__len__()`
- `obj1 == obj2` → calls `obj1.__eq__(obj2)`
- `obj1 + obj2` → calls `obj1.__add__(obj2)`

**Why they matter:** Magic methods let your custom classes behave like built-in types. When you implement `__str__`, `print()` works. When you implement `__len__`, `len()` works. Your class feels native to Python.

## String Representation: `__str__` and `__repr__`

### `__str__` — For End Users

`__str__` defines how your object looks when converted to a string (e.g., `print(obj)`, `str(obj)`).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Readable string representation for end users."""
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Alice, 30 years old
```

**Without `__str__`:**
```python
print(person)  # <__main__.Person object at 0x7f8b8c0d0a90>
```

### `__repr__` — For Developers

`__repr__` defines the "official" string representation, ideally one you could `eval()` to recreate the object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        """Unambiguous representation for developers."""
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        """Readable representation for end users."""
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)

print(person)       # Uses __str__: Alice, 30 years old
print(repr(person)) # Uses __repr__: Person(name='Alice', age=30)

# In the REPL, repr is used by default
>>> person
Person(name='Alice', age=30)
```

**When to implement:**
- Always implement `__repr__` for debugging
- Implement `__str__` if you need a user-friendly format
- If you only implement `__repr__`, it's used for both `repr()` and `str()`

## Comparison Methods

### `__eq__` — Equality

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Check if two points are equal."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

**Without `__eq__`:**
```python
print(p1 == p2)  # False — compares identity (id), not value
```

### Other Comparison Methods

```python
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

    def __le__(self, other):
        """Less than or equal."""
        return self.age <= other.age

    def __gt__(self, other):
        """Greater than if older."""
        return self.age > other.age

    def __ge__(self, other):
        """Greater than or equal."""
        return self.age >= other.age

alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice > bob)   # True (30 > 25)
print(bob < alice)   # True (25 < 30)
print(sorted([alice, bob], key=lambda p: p.age))  # [bob, alice]
```

## Arithmetic Methods

### Basic Operators

```python
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
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(-2, -2)
print(v1 * 3)   # Vector(3, 6)
```

**Common arithmetic methods:**
- `__add__(self, other)` — `+`
- `__sub__(self, other)` — `-`
- `__mul__(self, other)` — `*`
- `__truediv__(self, other)` — `/`
- `__floordiv__(self, other)` — `//`
- `__mod__(self, other)` — `%`
- `__pow__(self, other)` — `**`

## Container Methods

### `__len__` — Length

```python
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        """Return number of items."""
        return len(self.items)

inv = Inventory()
inv.add_item("sword")
inv.add_item("shield")

print(len(inv))  # 2
```

### `__getitem__` and `__setitem__` — Indexing

```python
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        """Get item by index: inv[0]."""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set item by index: inv[0] = 'new'."""
        self.items[index] = value

inv = Inventory()
inv.add_item("sword")
inv.add_item("shield")

print(inv[0])  # sword
print(inv[1])  # shield

inv[0] = "axe"
print(inv[0])  # axe

# Supports slicing for free
print(inv[0:2])  # ['axe', 'shield']
```

### `__iter__` — Iteration

```python
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        """Make inventory iterable."""
        return iter(self.items)

inv = Inventory()
inv.add_item("sword")
inv.add_item("shield")

for item in inv:
    print(item)
# sword
# shield
```

### `__contains__` — Membership

```python
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __contains__(self, item):
        """Check if item is in inventory: 'sword' in inv."""
        return item in self.items

inv = Inventory()
inv.add_item("sword")

print("sword" in inv)   # True
print("shield" in inv)  # False
```

## Context Manager: `__enter__` and `__exit__`

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"Opening connection to {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        print(f"Closing connection to {self.db_name}")
        return False  # Don't suppress exceptions

    def query(self, sql):
        print(f"Executing: {sql}")

# Usage with 'with' statement
with DatabaseConnection("mydb") as db:
    db.query("SELECT * FROM users")
# Opening connection to mydb
# Executing: SELECT * FROM users
# Closing connection to mydb
```

## Call Method: `__call__`

Makes an object callable like a function:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Called when you call the object: obj(x)."""
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## Complete Example: Point Class

Here's a complete `Point` class with multiple magic methods:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """User-friendly representation."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Developer representation."""
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """Check equality."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Add two points."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two points."""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply point by scalar."""
        return Point(self.x * scalar, self.y * scalar)

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)          # (1, 2)
print(repr(p1))    # Point(1, 2)
print(p1 == p2)    # False
print(p1 + p2)     # (4, 6)
print(p2 - p1)     # (2, 2)
print(p1 * 3)      # (3, 6)
```

## Mapping to Projects

**Project 5 (RPG Arena):**
```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        """User-friendly display."""
        return f"{self.name} (HP: {self.health})"

    def __repr__(self):
        """Developer display."""
        return f"Character(name='{self.name}', health={self.health})"

    def __eq__(self, other):
        """Characters are equal if same name."""
        return self.name == other.name

    def __lt__(self, other):
        """Compare by health for sorting."""
        return self.health < other.health
```

**Project 6 (IMS):**
```python
class Inventory:
    def __init__(self):
        self.products = []

    def __len__(self):
        """Return number of products."""
        return len(self.products)

    def __getitem__(self, index):
        """Access products by index."""
        return self.products[index]

    def __iter__(self):
        """Iterate over products."""
        return iter(self.products)

    def __contains__(self, product_name):
        """Check if product exists."""
        return any(p.name == product_name for p in self.products)
```

## Common Magic Methods Reference

| Category | Methods | Usage |
|---|---|---|
| **String representation** | `__str__`, `__repr__` | `print(obj)`, `str(obj)`, `repr(obj)` |
| **Comparison** | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` | `==`, `!=`, `<`, `<=`, `>`, `>=` |
| **Arithmetic** | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **Container** | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__` | `len()`, `obj[i]`, `obj[i] = x`, `del obj[i]`, `x in obj`, `for x in obj` |
| **Context manager** | `__enter__`, `__exit__` | `with obj:` |
| **Callable** | `__call__` | `obj()` |

## Key Takeaways

- **Magic methods** let your classes behave like built-in types
- **`__str__` for users**, `__repr__` for developers
- **`__eq__` and comparison methods** enable `==`, `<`, `>`, etc.
- **`__add__`, `__sub__`, etc.** enable arithmetic operators
- **`__len__`, `__getitem__`, `__iter__`** make your class container-like
- **Always implement `__repr__`** for debugging
- **Implement magic methods to make your API Pythonic**, not Java-like

Next: [Code Demos](./code/)
