# Abstraction and Abstract Base Classes

## What Abstraction Means

**Abstraction:** Hide complexity, show only what's essential.

In OOP, abstraction means defining **what** a class should do without specifying **how**. An abstract class defines an interface (methods that must exist) but leaves the implementation to subclasses.

## Why Use Abstract Base Classes

**Problem:** You're building Project 5 (RPG Arena) and want to ensure every character type has an `attack()` method. But inheritance alone doesn't enforce this:

```python
class Character:
    def attack(self, target):
        raise NotImplementedError("Subclass must implement attack()")

class Warrior(Character):
    def attack(self, target):
        target.health -= self.attack_power

class Mage(Character):
    pass  # ❌ Forgot to implement attack()!

# No error until you try to use it
mage = Mage()
# mage.attack(target)  # RuntimeError: NotImplementedError
```

**Solution: Abstract Base Classes (ABCs)**

ABCs **enforce** that subclasses implement required methods. If a subclass forgets, you get an error **when you try to instantiate it**, not later.

## The `abc` Module

Python's `abc` module provides tools for defining abstract base classes:

```python
from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class for all characters."""

    @abstractmethod
    def attack(self, target):
        """Subclasses must implement this."""
        pass

class Warrior(Character):
    def attack(self, target):
        target.health -= self.attack_power

class Mage(Character):
    pass  # ❌ Forgot to implement attack()

# This works
warrior = Warrior()

# This fails immediately
# mage = Mage()
# TypeError: Can't instantiate abstract class Mage with abstract method attack
```

**Key difference:** With ABCs, you get an error **when you create the instance**, not when you call the method. This catches bugs earlier.

## Basic ABC Syntax

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area. Subclasses must implement."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter. Subclasses must implement."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Usage
circle = Circle(5)
square = Square(4)

print(f"Circle area: {circle.area()}")
print(f"Square area: {square.area()}")
```

**Anatomy:**
- `class Shape(ABC):` — Inherit from `ABC`
- `@abstractmethod` — Decorator marks a method as abstract
- Subclasses must implement all abstract methods to be instantiable

## Abstract Methods with Implementation

Abstract methods can have default implementations. Subclasses must override them, but can call `super()` to get the default:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        """Default implementation."""
        return "Some sound"

class Dog(Animal):
    def speak(self):
        # Call parent's implementation, then extend
        base_sound = super().speak()
        return f"{base_sound} - Woof!"

dog = Dog()
print(dog.speak())  # Some sound - Woof!
```

## Mixing Abstract and Concrete Methods

ABCs can have both abstract methods (must override) and concrete methods (can use as-is):

```python
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, target):
        """Subclasses must implement."""
        pass

    def is_alive(self):
        """Concrete method — no need to override."""
        return self.health > 0

    def describe(self):
        """Concrete method."""
        return f"{self.name} (HP: {self.health})"

class Warrior(Character):
    def attack(self, target):
        target.health -= 20

warrior = Warrior("Conan", 100)
print(warrior.describe())  # Uses inherited concrete method
print(warrior.is_alive())  # Uses inherited concrete method
```

## When to Use ABCs

**Use ABCs when:**
1. You have a family of classes that share an interface
2. You want to enforce that subclasses implement certain methods
3. You're building a framework or library that others will extend

**Don't use ABCs when:**
1. You have a simple class that doesn't need subclassing
2. Duck typing is sufficient (most of the time in Python)
3. The overhead of `abc` isn't worth it for a small project

**Python's philosophy:** Duck typing is preferred. ABCs are for when you **really** need to enforce an interface.

## ABCs in the Wild

Python's standard library uses ABCs extensively:

```python
from collections.abc import Iterable, Sized

class MyCollection(Iterable, Sized):
    def __iter__(self):
        return iter([1, 2, 3])

    def __len__(self):
        return 3

# MyCollection is now recognized as iterable and sized
coll = MyCollection()
print(list(coll))  # [1, 2, 3]
print(len(coll))   # 3
```

**Common ABCs in `collections.abc`:**
- `Iterable` — requires `__iter__`
- `Iterator` — requires `__iter__` and `__next__`
- `Sized` — requires `__len__`
- `Container` — requires `__contains__`
- `Sequence` — requires `__getitem__`, `__len__`, etc.

## Mapping to Projects

**Project 5 (RPG Arena):**
```python
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def special_ability(self, target):
        """Each character type has a unique special ability."""
        pass

    def attack(self, target):
        """Base attack — all characters can use this."""
        target.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def special_ability(self, target):
        """Shield bash — stuns and damages."""
        target.health -= self.attack_power * 1.5

class Mage(Character):
    def special_ability(self, target):
        """Fireball — area damage."""
        target.health -= self.attack_power * 2
```

**Project 6 (IMS):**
```python
from abc import ABC, abstractmethod

class Discountable(ABC):
    """Interface for objects that can have discounts."""

    @abstractmethod
    def apply_discount(self, percentage):
        """Apply a discount. Return new price."""
        pass

class Product(Discountable):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        return self.price * (1 - percentage / 100)

class Invoice(Discountable):
    def __init__(self, items):
        self.items = items

    def apply_discount(self, percentage):
        total = sum(item.price for item in self.items)
        return total * (1 - percentage / 100)
```

## ABCs vs Protocols (Python 3.8+)

Python 3.8 introduced **Protocols** (PEP 544) for structural subtyping:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

# No need to inherit from Drawable
class Circle:
    def draw(self) -> str:
        return "Drawing circle"

# Works because Circle has a .draw() method
def render(shape: Drawable):
    print(shape.draw())

render(Circle())  # Works!
```

**Protocols vs ABCs:**
- **ABCs:** Explicit inheritance (`class Dog(Animal)`)
- **Protocols:** Structural typing (if it has the right methods, it's compatible)

**For this course, stick with ABCs.** Protocols are more advanced and not widely used yet.

## Key Takeaways

- **Abstraction hides complexity**, shows only essential interface
- **Abstract Base Classes (ABCs)** enforce that subclasses implement required methods
- **Use `abc.ABC` and `@abstractmethod`** to define abstract classes
- **Subclasses must implement all abstract methods** to be instantiable
- **ABCs can mix abstract and concrete methods**
- **Use ABCs when you need to enforce an interface**, not for every class
- **Python prefers duck typing** — ABCs are for when enforcement is important

Next: [Magic Methods](./03-magic-methods.md)
