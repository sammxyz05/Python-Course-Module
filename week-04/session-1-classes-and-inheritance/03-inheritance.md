# Inheritance

## Why Inheritance Matters

Imagine you're building Project 5 (RPG Arena) with three character types: Warrior, Mage, Archer. They all share:
- A name
- Health points
- An attack method

But they differ in:
- Special abilities (Warrior has Shield Bash, Mage has Fireball, Archer has Quick Shot)
- How their attack is calculated

**Without inheritance, you duplicate code:**
```python
class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self):
        return 20  # Warrior base damage

class Mage:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self):
        return 15  # Mage base damage
```

Notice the duplication: `__init__` is identical. **Inheritance eliminates this.**

## Basic Inheritance Syntax

```python
# Base class (parent, superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def describe(self):
        return f"{self.name} is a {self.species}"

# Derived class (child, subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canis familiaris")
        self.breed = breed
    
    def bark(self):
        return "Woof!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.describe())  # Buddy is a Canis familiaris (inherited method)
print(dog.bark())      # Woof! (Dog's own method)
print(dog.name)        # Buddy (inherited attribute)
print(dog.breed)       # Golden Retriever (Dog's own attribute)
```

**Anatomy:**
- `class Dog(Animal):` — `Dog` inherits from `Animal`
- `super().__init__(...)` — Call the parent's `__init__` to initialize inherited attributes
- `Dog` gets all of `Animal`'s methods and attributes
- `Dog` can add its own methods (`bark`) and attributes (`breed`)

## Understanding `super()`

**`super()` calls the parent class's method.**

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__ called for {name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call Animal's __init__
        self.breed = breed
        print(f"Dog.__init__ called for {name}")

dog = Dog("Buddy", "Golden Retriever")
# Output:
# Animal.__init__ called for Buddy
# Dog.__init__ called for Buddy
```

**Why use `super()`?**
- Ensures the parent class is properly initialized
- Lets you extend the parent's behavior without duplicating code
- Works correctly with multiple inheritance (advanced topic, not covered this week)

**Common mistake — forgetting `super()`:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, breed):
        # ❌ Forgot to call super().__init__()
        self.breed = breed

dog = Dog("Golden Retriever")
# print(dog.name)  # AttributeError: 'Dog' object has no attribute 'name'
```

## Method Overriding

**Subclasses can replace (override) parent methods:**

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):  # Override parent's speak
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override parent's speak
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

**When to override:**
- The parent's method does the wrong thing for the subclass
- The subclass needs specialized behavior

## Extending Parent Methods

Sometimes you want to **add to** the parent's behavior, not replace it:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"This is {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def describe(self):
        # Call parent's describe, then add more
        base_description = super().describe()
        return f"{base_description}, a {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.describe())
# This is Buddy, a Golden Retriever
```

**Pattern:**
1. Call `super().method()` to get the parent's result
2. Extend or modify the result
3. Return the new result

## The `is-a` Relationship

**Use inheritance when the subclass "is a" type of the parent.**

✅ Good examples:
- `Dog` is an `Animal`
- `Warrior` is a `Character`
- `CheckingAccount` is a `BankAccount`

❌ Bad examples:
- `Car` is NOT a `Wheel` (a car *has* wheels — use composition, not inheritance)
- `Student` is NOT a `Course` (a student *takes* courses)

**Inheritance models "is-a". Composition models "has-a".**

## Multiple Levels of Inheritance

You can inherit from a class that itself inherits:

```python
class LivingThing:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        return f"{self.name} breathes"

class Animal(LivingThing):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    
    def move(self):
        return f"{self.name} moves"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canis familiaris")
        self.breed = breed
    
    def bark(self):
        return "Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.breathe())  # Buddy breathes (from LivingThing)
print(dog.move())     # Buddy moves (from Animal)
print(dog.bark())     # Woof! (from Dog)
```

**Keep hierarchies shallow.** Deep inheritance (more than 2-3 levels) gets hard to understand and maintain.

## Checking Inheritance

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance() — is this object an instance of this class (or a subclass)?
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog is a subclass of Animal)

# issubclass() — is this class a subclass of another class?
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

## Common Inheritance Patterns

**1. Template Method Pattern**

Parent defines the structure, subclasses fill in details:

```python
class Report:
    def generate(self):
        """Template method — defines the structure."""
        self.print_header()
        self.print_body()
        self.print_footer()
    
    def print_header(self):
        """Default header."""
        print("=== Report ===")
    
    def print_body(self):
        """Must be overridden by subclass."""
        raise NotImplementedError("Subclass must implement print_body")
    
    def print_footer(self):
        """Default footer."""
        print("=== End ===")

class SalesReport(Report):
    def print_body(self):
        print("Sales data here...")

report = SalesReport()
report.generate()
# === Report ===
# Sales data here...
# === End ===
```

**2. Specialized Subclasses**

Base class provides common functionality, subclasses add specialization:

```python
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        """Base attack."""
        target.health -= self.attack_power

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
    
    def shield_bash(self, target):
        """Warrior special ability."""
        target.health -= self.attack_power * 1.5

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=15)
    
    def fireball(self, target):
        """Mage special ability."""
        target.health -= self.attack_power * 2
```

## When NOT to Use Inheritance

**Don't use inheritance just to reuse code.** Use it when there's a clear "is-a" relationship.

**Bad example:**
```python
# ❌ WRONG: User is NOT a Database
class User(Database):
    def save(self):
        self.execute("INSERT INTO users ...")
```

**Good example:**
```python
# ✅ CORRECT: User HAS a database (composition)
class User:
    def __init__(self, db):
        self.db = db
    
    def save(self):
        self.db.execute("INSERT INTO users ...")
```

**Prefer composition over inheritance** when the relationship is "has-a" or "uses-a".

## Mapping to Projects

**Project 5 (RPG Arena):**
```python
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        target.health -= self.attack_power
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
    
    def shield_bash(self, target):
        target.health -= self.attack_power * 1.5

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=15)
    
    def fireball(self, target):
        target.health -= self.attack_power * 2
```

**Project 6 (IMS):**
- Might use inheritance for different product types (`PerishableProduct`, `ElectronicProduct`)
- Or for different invoice types (`RetailInvoice`, `WholesaleInvoice`)

## Key Takeaways

- **Inheritance models "is-a" relationships** — `Dog` is an `Animal`
- **Use `class Child(Parent):`** to inherit from a base class
- **Call `super().__init__()`** in the child's `__init__` to initialize the parent
- **Subclasses inherit all methods and attributes** from the parent
- **Override methods** to specialize behavior in the subclass
- **Extend methods** by calling `super().method()` and adding to the result
- **`isinstance(obj, Class)`** checks if an object is an instance of a class (or subclass)
- **Prefer composition over inheritance** when the relationship is "has-a"

Next: [Session 2 — Polymorphism and Abstraction](../session-2-polymorphism-abstraction/README.md)
