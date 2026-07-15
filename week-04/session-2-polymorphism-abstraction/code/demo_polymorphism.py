"""
Demo: Polymorphism
Shows: method overriding, duck typing, polymorphic behavior
"""

# Method overriding — same method name, different behavior
print("=== Method Overriding ===")

class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Same method name, different implementations
animals = [Dog(), Cat(), Cow(), Animal()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")


# Duck typing — objects don't need to inherit from a common base
print("\n=== Duck Typing ===")

class Robot:
    def speak(self):
        return "Beep boop"

class Human:
    def speak(self):
        return "Hello!"

# Robot and Human aren't related to Animal, but they have .speak()
things = [Dog(), Robot(), Human()]

for thing in things:
    print(f"{thing.__class__.__name__}: {thing.speak()}")


# Polymorphism in functions
print("\n=== Polymorphic Functions ===")

def make_it_speak(thing):
    """Works with any object that has a .speak() method."""
    print(f"It says: {thing.speak()}")

make_it_speak(Dog())
make_it_speak(Robot())
make_it_speak(Human())


# Real-world example: file-like objects
print("\n=== File-like Objects (Polymorphism in Action) ===")

from io import StringIO

def count_lines(file_obj):
    """Count lines in any file-like object."""
    lines = file_obj.readlines()
    return len(lines)

# Works with in-memory file
fake_file = StringIO("line1\nline2\nline3\nline4")
print(f"Lines in fake file: {count_lines(fake_file)}")

# Would also work with real files:
# with open("data.txt") as f:
#     print(f"Lines in real file: {count_lines(f)}")


# Polymorphism with different implementations
print("\n=== Different Implementations ===")

class Character:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def attack(self, target):
        """Base attack."""
        damage = self.attack_power
        print(f"{self.name} attacks {target} for {damage} damage")
        return damage

class Warrior(Character):
    def attack(self, target):
        """Warriors do extra damage."""
        damage = self.attack_power * 1.2
        print(f"{self.name} attacks {target} with a powerful strike for {damage:.1f} damage!")
        return damage

class Mage(Character):
    def attack(self, target):
        """Mages cast spells."""
        damage = self.attack_power * 0.8
        print(f"{self.name} casts a spell at {target} for {damage:.1f} damage!")
        return damage

class Archer(Character):
    def attack(self, target):
        """Archers shoot arrows."""
        damage = self.attack_power * 1.0
        print(f"{self.name} shoots an arrow at {target} for {damage} damage!")
        return damage

# Combat function works with any character type
def battle_attack(attacker, defender_name):
    """Generic battle function that works with any character."""
    attacker.attack(defender_name)

warrior = Warrior("Conan", 20)
mage = Mage("Gandalf", 15)
archer = Archer("Legolas", 18)

battle_attack(warrior, "Goblin")
battle_attack(mage, "Dragon")
battle_attack(archer, "Orc")


# Polymorphism without type checking
print("\n=== No Type Checking Needed ===")

def process_items(items):
    """Process any iterable of items with .speak()."""
    for item in items:
        # No isinstance() check — just call the method
        print(item.speak())

mixed_things = [Dog(), Cat(), Robot(), Human()]
process_items(mixed_things)
