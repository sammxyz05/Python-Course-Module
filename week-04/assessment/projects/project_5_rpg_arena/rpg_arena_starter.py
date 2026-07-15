"""
Project 5: RPG Arena (Optional Warmup)
A turn-based combat simulator demonstrating OOP concepts.

This is a starter template. Follow the PROJECT_SPEC.md for detailed requirements.
"""

from abc import ABC, abstractmethod
import random


# TODO 1: Define Character abstract base class
# Requirements:
# - Inherit from ABC
# - __init__ takes name, health, attack_power
# - Store name, _health (protected), _max_health, attack_power
# - Abstract method: attack(opponent)
# - Method: take_damage(damage) - reduces health, min 0
# - Method: is_alive() - returns True if health > 0
# - Method: get_health() - returns current health
# - Magic method: __str__ - returns "{name}: {health}/{max_health} HP"

class Character(ABC):
    """Abstract base class for all characters."""
    pass  # Replace with your code


# TODO 2: Create Warrior class
# Requirements:
# - Inherit from Character
# - __init__ takes name, calls super().__init__(name, health=150, attack_power=20)
# - Implement attack(opponent) - deals attack_power damage, returns attack message

class Warrior(Character):
    """Warrior: High health, medium damage."""
    pass  # Replace with your code


# TODO 3: Create Mage class
# Requirements:
# - Inherit from Character
# - __init__ takes name, calls super().__init__(name, health=80, attack_power=35)
# - Implement attack(opponent) - deals attack_power damage, returns attack message

class Mage(Character):
    """Mage: Low health, high damage."""
    pass  # Replace with your code


# TODO 4: Create Archer class
# Requirements:
# - Inherit from Character
# - __init__ takes name, calls super().__init__(name, health=100, attack_power=25)
# - Add dodge_chance attribute (0.2 = 20%)
# - Implement attack(opponent) - 10% crit chance (double damage), returns attack message
# - Override take_damage(damage) - 20% chance to dodge (no damage taken)

class Archer(Character):
    """Archer: Medium health, medium damage, can dodge."""
    pass  # Replace with your code


# TODO 5: Implement combat system
# Requirements:
# - Takes two Character objects
# - Alternates turns until one character dies
# - Prints turn number, attack message, health status
# - Returns winner

def combat(character1, character2):
    """
    Simulate turn-based combat between two characters.

    Args:
        character1: First Character instance
        character2: Second Character instance

    Returns:
        Character: The winner
    """
    pass  # Replace with your code


# TODO 6: Implement main game loop
# Requirements:
# - Print welcome message
# - Display character selection menu
# - Get player choice and name
# - Create player character based on choice
# - Create random opponent
# - Run combat
# - Display winner message

def main():
    """Main game loop."""
    print("=" * 50)
    print("       Welcome to RPG Arena!")
    print("=" * 50)

    # Your code here
    pass


if __name__ == "__main__":
    main()


# TESTING SECTION (uncomment to test individual components)
# ========================================================

# Test 1: Verify Character is abstract (should raise TypeError)
# try:
#     char = Character("Test", 100, 10)
#     print("ERROR: Character should not be instantiable!")
# except TypeError as e:
#     print(f"✓ Correct: {e}")

# Test 2: Create Warrior
# warrior = Warrior("Thor")
# print(warrior)  # Expected: Thor: 150/150 HP
# print(f"Is alive: {warrior.is_alive()}")  # Expected: True

# Test 3: Test take_damage
# warrior.take_damage(50)
# print(warrior)  # Expected: Thor: 100/150 HP
# warrior.take_damage(200)  # Should cap at 0
# print(warrior)  # Expected: Thor: 0/150 HP
# print(f"Is alive: {warrior.is_alive()}")  # Expected: False

# Test 4: Create Mage
# mage = Mage("Gandalf")
# print(mage)  # Expected: Gandalf: 80/80 HP

# Test 5: Create Archer
# archer = Archer("Legolas")
# print(archer)  # Expected: Legolas: 100/100 HP

# Test 6: Test polymorphic combat (all characters use same attack interface)
# warrior = Warrior("Conan")
# mage = Mage("Merlin")
# print(warrior.attack(mage))  # Should print attack message
# print(mage)  # Should show reduced health

# Test 7: Test full combat
# player = Warrior("Hero")
# opponent = Mage("Villain")
# winner = combat(player, opponent)
# print(f"Winner: {winner.name}")

# Test 8: Test Archer dodge (run multiple times to see dodge in action)
# archer = Archer("Robin")
# warrior = Warrior("Enemy")
# for i in range(10):
#     print(f"\nTest {i+1}:")
#     archer._health = 100  # Reset health
#     warrior.attack(archer)
#     print(archer)
