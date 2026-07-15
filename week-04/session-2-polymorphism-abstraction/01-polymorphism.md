# Polymorphism

## What Polymorphism Means

**Polymorphism:** "Many forms" — the same interface, different implementations.

In OOP, polymorphism means different classes can have methods with the same name, but different behavior. This lets you write code that works with many types of objects without knowing their specific class.

## Method Overriding (Subtype Polymorphism)

The most common form of polymorphism: subclasses override parent methods.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Same method name, different behavior
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Some generic sound
```

**Key insight:** The loop doesn't need to know whether it's a `Dog`, `Cat`, or `Animal`. It just calls `.speak()` and gets the right behavior.

## Duck Typing

**"If it walks like a duck and quacks like a duck, it's a duck."**

Python doesn't care about the type hierarchy. It only cares that the object has the methods you're calling.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep boop"

# Dog and Robot aren't related by inheritance
# But they both have .speak(), so they're polymorphic

things = [Dog(), Robot()]

for thing in things:
    print(thing.speak())
# Woof!
# Beep boop
```

**This is duck typing:** Python doesn't check `isinstance(thing, Animal)`. It just tries to call `.speak()`. If the object has that method, it works. If not, you get an `AttributeError`.

## Polymorphism in Functions

You can write functions that work with any object that has the right interface:

```python
def make_it_speak(thing):
    """Works with any object that has a .speak() method."""
    print(thing.speak())

make_it_speak(Dog())   # Woof!
make_it_speak(Robot()) # Beep boop
```

**No type checking needed.** The function doesn't care what `thing` is, only that it has `.speak()`.

## Why Polymorphism Matters

**Example: File-like objects**

Python's `file` object has `.read()`, `.write()`, `.close()`. But many other objects have the same interface:
- `io.StringIO` (in-memory file)
- `urllib.request.urlopen(url)` (HTTP response)
- `gzip.open(filename)` (compressed file)

Functions that accept a "file-like object" work with all of them:

```python
def count_lines(file_obj):
    """Count lines in any file-like object."""
    return len(file_obj.readlines())

# Works with all of these:
with open("data.txt") as f:
    print(count_lines(f))

from io import StringIO
fake_file = StringIO("line1\nline2\nline3")
print(count_lines(fake_file))
```

**This is polymorphism in action.** One function, many implementations.

## Polymorphism in Projects

**Project 5 (RPG Arena):**
```python
class Character:
    def attack(self, target):
        target.health -= self.attack_power

class Warrior(Character):
    def attack(self, target):
        # Different implementation — warriors do extra damage
        target.health -= self.attack_power * 1.2

class Mage(Character):
    def attack(self, target):
        # Different implementation — mages do magic damage
        target.health -= self.attack_power * 0.8

# Combat loop works with any character type
def battle(char1, char2):
    while char1.is_alive() and char2.is_alive():
        char1.attack(char2)  # Calls the right attack() for char1's type
        if char2.is_alive():
            char2.attack(char1)
```

**Project 6 (IMS):**
```python
class Product:
    def get_total_value(self):
        return self.price * self.quantity

class PerishableProduct(Product):
    def get_total_value(self):
        # Different implementation — apply discount if near expiry
        base_value = super().get_total_value()
        if self.days_until_expiry < 7:
            return base_value * 0.8
        return base_value

# Inventory calculation works with any product type
def calculate_inventory_value(products):
    return sum(p.get_total_value() for p in products)
```

## Method Overriding Rules

**When you override a method:**
1. **Same name** as parent's method
2. **Same or compatible signature** (parameters)
3. **Can call parent's method** with `super()`

```python
class Vehicle:
    def start(self):
        return "Starting vehicle..."

class Car(Vehicle):
    def start(self):
        # Call parent's method, then extend
        base_message = super().start()
        return f"{base_message} and engaging gear"
```

## Common Polymorphic Interfaces

**Iterator protocol:** Objects with `__iter__` and `__next__`
```python
for item in obj:
    # Works with list, tuple, dict, set, file, custom classes
    pass
```

**Context manager protocol:** Objects with `__enter__` and `__exit__`
```python
with obj as x:
    # Works with files, locks, database connections, custom classes
    pass
```

**Comparison protocol:** Objects with `__eq__`, `__lt__`, etc.
```python
if obj1 < obj2:
    # Works with int, float, str, datetime, custom classes
    pass
```

## Type Checking vs Duck Typing

**Explicit type checking (discouraged):**
```python
# ❌ WRONG: checks exact type
def make_it_speak(thing):
    if isinstance(thing, Dog):
        print(thing.speak())
    elif isinstance(thing, Cat):
        print(thing.speak())
    # What about Robot? You forgot it!
```

**Duck typing (Pythonic):**
```python
# ✅ CORRECT: just call the method
def make_it_speak(thing):
    print(thing.speak())
```

**When to use `isinstance()`:**
- You need different logic for different types
- You're validating input at API boundaries
- You're handling multiple possible interfaces (e.g., accepts `str` or `list`)

## Mapping to Week 3 Concepts

Think of polymorphism as **the OOP version of higher-order functions**:

| Week 3 | Week 4 |
|---|---|
| `sorted(items, key=lambda x: x['price'])` | `items.sort()` (objects implement `__lt__`) |
| `filter(lambda x: x > 0, values)` | `[v for v in values if v > 0]` (objects implement `__gt__`) |
| `map(str.upper, words)` | `[w.upper() for w in words]` (all strings have `.upper()`) |

In Week 3, you passed functions to customize behavior. In Week 4, you define methods on classes to customize behavior.

## Key Takeaways

- **Polymorphism:** Same method name, different implementations
- **Method overriding:** Subclass replaces parent's method
- **Duck typing:** Python cares about interface (methods), not type hierarchy
- **Write functions that accept any object with the right methods** (don't check types)
- **Polymorphism enables generic algorithms** (sort, filter, iterate, etc.)
- **Python's built-in protocols** (iterator, context manager, comparison) are all polymorphic

Next: [Abstraction and Abstract Base Classes](./02-abstraction-abc.md)
