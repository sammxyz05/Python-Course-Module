"""
Demo: Instance vs Class Attributes
Shows: the difference between instance attributes and class attributes
"""

class Dog:
    # Class attribute — shared by all dogs
    species = "Canis familiaris"
    count = 0  # Counter for number of dogs created

    def __init__(self, name, age):
        # Instance attributes — unique to each dog
        self.name = name
        self.age = age
        # Increment class counter
        Dog.count += 1

    def describe(self):
        """Describe this dog."""
        return f"{self.name} is {self.age} years old and is a {self.species}"


# Create instances
print("=== Creating dogs ===")
buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)
luna = Dog("Luna", 2)

# Instance attributes are per-dog
print(buddy.name)     # Buddy
print(max_dog.name)   # Max
print(luna.name)      # Luna

# Class attributes are shared
print("\n=== Class attributes (shared) ===")
print(f"Buddy's species: {buddy.species}")
print(f"Max's species: {max_dog.species}")
print(f"Luna's species: {luna.species}")

# Change class attribute — affects all instances
print("\n=== Changing class attribute ===")
Dog.species = "Canis lupus familiaris"
print(f"Buddy's species: {buddy.species}")
print(f"Max's species: {max_dog.species}")

# Class counter
print(f"\n=== Total dogs created: {Dog.count} ===")

# Trap: instance attribute shadows class attribute
print("\n=== Instance attribute shadowing ===")
buddy.species = "Super Dog"  # Creates an instance attribute
print(f"Buddy's species: {buddy.species}")  # Super Dog (instance attribute)
print(f"Max's species: {max_dog.species}")  # Canis lupus familiaris (class attribute)

# Common mistake: mutable class attribute
print("\n=== DANGER: Mutable class attributes ===")

class BadCart:
    items = []  # ❌ WRONG: shared across all instances!

    def add_item(self, item):
        self.items.append(item)

cart1 = BadCart()
cart2 = BadCart()

cart1.add_item("apple")
print(f"Cart 1: {cart1.items}")  # ['apple']
print(f"Cart 2: {cart2.items}")  # ['apple'] — SURPRISE! Both carts share the same list

class GoodCart:
    def __init__(self):
        self.items = []  # ✅ CORRECT: each cart gets its own list

    def add_item(self, item):
        self.items.append(item)

cart3 = GoodCart()
cart4 = GoodCart()

cart3.add_item("banana")
print(f"\nCart 3: {cart3.items}")  # ['banana']
print(f"Cart 4: {cart4.items}")    # [] — correctly separate
