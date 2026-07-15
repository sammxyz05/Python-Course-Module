# Project 5: RPG Arena (Optional Warmup)

## Overview

Build a turn-based combat simulator demonstrating OOP fundamentals: abstract base classes, inheritance, polymorphism, encapsulation, and magic methods.

⚠️ **This project is OPTIONAL and UNGRADED.** Do it if:
- OOP concepts feel unclear
- You want practice before Project 6 (IMS)
- You learn better by building something fun first

If OOP feels solid, skip this and go straight to Project 6.

**Estimated time:** 3-4 hours  
**Status:** Warmup exercise, not graded

## Learning Objectives

- Use abstract base classes (ABC) to define interfaces
- Implement inheritance with `super()`
- Demonstrate polymorphism (different characters, same interface)
- Use magic methods (`__str__`, `__repr__`)
- Practice encapsulation (private attributes)

## Requirements

### Core Features

Your RPG Arena must support:

1. **Abstract Character base class** with abstract `attack()` method
2. **Three concrete character types:**
   - **Warrior:** High health, medium damage
   - **Mage:** Low health, high damage
   - **Archer:** Medium health, medium damage, chance to dodge
3. **Combat system:**
   - Turn-based combat between two characters
   - Characters attack each other until one's health reaches 0
   - Display combat log showing each action
4. **Character selection:** Player chooses character type before combat starts

### Technical Requirements

#### 1. Character Base Class (Abstract)

```python
from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class for all characters."""
    
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health  # Protected attribute
        self._max_health = health
        self.attack_power = attack_power
    
    @abstractmethod
    def attack(self, opponent):
        """
        Attack opponent. Must be implemented by subclasses.
        Returns attack message string.
        """
        pass
    
    def take_damage(self, damage):
        """Reduce health by damage amount."""
        self._health = max(0, self._health - damage)
    
    def is_alive(self):
        """Return True if health > 0."""
        return self._health > 0
    
    def get_health(self):
        """Return current health."""
        return self._health
    
    def __str__(self):
        """Return string representation."""
        return f"{self.name}: {self._health}/{self._max_health} HP"
```

#### 2. Warrior Class

```python
class Warrior(Character):
    """Warrior: High health, medium damage."""
    
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    def attack(self, opponent):
        """Strong melee attack."""
        opponent.take_damage(self.attack_power)
        return f"{self.name} swings their sword at {opponent.name} for {self.attack_power} damage!"
```

#### 3. Mage Class

```python
class Mage(Character):
    """Mage: Low health, high damage, can cast fireball."""
    
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=35)
    
    def attack(self, opponent):
        """Powerful magic attack."""
        opponent.take_damage(self.attack_power)
        return f"{self.name} casts fireball at {opponent.name} for {self.attack_power} damage!"
```

#### 4. Archer Class

```python
import random

class Archer(Character):
    """Archer: Medium health, medium damage, 20% chance to dodge."""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)
        self.dodge_chance = 0.2
    
    def attack(self, opponent):
        """Ranged attack with chance to crit."""
        damage = self.attack_power
        if random.random() < 0.1:  # 10% crit chance
            damage *= 2
            message = f"{self.name} lands a CRITICAL arrow shot on {opponent.name} for {damage} damage!"
        else:
            message = f"{self.name} shoots an arrow at {opponent.name} for {damage} damage!"
        
        opponent.take_damage(damage)
        return message
    
    def take_damage(self, damage):
        """Override to add dodge chance."""
        if random.random() < self.dodge_chance:
            print(f"  → {self.name} dodges the attack!")
            return
        super().take_damage(damage)
```

### Combat System

```python
def combat(character1, character2):
    """
    Simulate turn-based combat between two characters.
    Returns the winner.
    """
    print(f"\n⚔️  {character1.name} vs {character2.name} ⚔️\n")
    
    turn = 1
    attacker, defender = character1, character2
    
    while character1.is_alive() and character2.is_alive():
        print(f"Turn {turn}:")
        
        # Attacker attacks defender
        attack_message = attacker.attack(defender)
        print(f"  {attack_message}")
        
        # Show health status
        print(f"  {defender}")
        
        # Swap attacker and defender
        attacker, defender = defender, attacker
        
        turn += 1
        print()
    
    # Determine winner
    winner = character1 if character1.is_alive() else character2
    print(f"🏆 {winner.name} wins the battle!\n")
    return winner
```

### Main Loop

```python
def main():
    """Main game loop."""
    print("=" * 50)
    print("       Welcome to RPG Arena!")
    print("=" * 50)
    
    # Player chooses character
    print("\nChoose your character:")
    print("1. Warrior (High HP, Medium Damage)")
    print("2. Mage (Low HP, High Damage)")
    print("3. Archer (Medium HP, Medium Damage, Dodge Chance)")
    
    choice = input("\nEnter 1, 2, or 3: ").strip()
    
    player_name = input("Enter your character's name: ").strip()
    
    # Create player character
    if choice == "1":
        player = Warrior(player_name)
    elif choice == "2":
        player = Mage(player_name)
    elif choice == "3":
        player = Archer(player_name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior(player_name)
    
    # Create opponent (random)
    opponent_type = random.choice([Warrior, Mage, Archer])
    opponent = opponent_type("Evil " + opponent_type.__name__)
    
    # Start combat
    winner = combat(player, opponent)
    
    if winner == player:
        print("Congratulations! You won!")
    else:
        print("You were defeated. Better luck next time!")


if __name__ == "__main__":
    main()
```

## Implementation Guide

### Step 1: Create Character Base Class

1. Import `ABC` and `abstractmethod` from `abc` module
2. Define `Character(ABC)` with `__init__`, abstract `attack()`, `take_damage()`, `is_alive()`, `get_health()`, `__str__`
3. Test that you CANNOT instantiate `Character` directly (should raise TypeError)

### Step 2: Create Concrete Subclasses

1. Create `Warrior`, `Mage`, and `Archer` classes
2. Each must:
   - Inherit from `Character`
   - Call `super().__init__()` with appropriate stats
   - Implement `attack()` method (required by ABC)
3. Test each character individually

### Step 3: Implement Combat System

1. Create `combat(character1, character2)` function
2. Use polymorphism: both characters use same `attack()` interface
3. Test combat between different character combinations

### Step 4: Add Main Loop

1. Create character selection menu
2. Create random opponent
3. Start combat
4. Display winner

### Step 5: Test Edge Cases

- Verify abstract class cannot be instantiated
- Test all character type combinations in combat
- Verify dodge mechanics work for Archer
- Verify health never goes below 0

## Example Output

```
==================================================
       Welcome to RPG Arena!
==================================================

Choose your character:
1. Warrior (High HP, Medium Damage)
2. Mage (Low HP, High Damage)
3. Archer (Medium HP, Medium Damage, Dodge Chance)

Enter 1, 2, or 3: 2
Enter your character's name: Gandalf

⚔️  Gandalf vs Evil Warrior ⚔️

Turn 1:
  Gandalf casts fireball at Evil Warrior for 35 damage!
  Evil Warrior: 115/150 HP

Turn 2:
  Evil Warrior swings their sword at Gandalf for 20 damage!
  Gandalf: 60/80 HP

Turn 3:
  Gandalf casts fireball at Evil Warrior for 35 damage!
  Evil Warrior: 80/150 HP

Turn 4:
  Evil Warrior swings their sword at Gandalf for 20 damage!
  Gandalf: 40/80 HP

Turn 5:
  Gandalf casts fireball at Evil Warrior for 35 damage!
  Evil Warrior: 45/150 HP

Turn 6:
  Evil Warrior swings their sword at Gandalf for 20 damage!
  Gandalf: 20/80 HP

Turn 7:
  Gandalf casts fireball at Evil Warrior for 35 damage!
  Evil Warrior: 10/150 HP

Turn 8:
  Evil Warrior swings their sword at Gandalf for 20 damage!
  Gandalf: 0/80 HP

🏆 Evil Warrior wins the battle!

You were defeated. Better luck next time!
```

## Testing Checklist

- [ ] Cannot instantiate `Character` directly (raises TypeError)
- [ ] All three character types can be created
- [ ] Each character's `attack()` method works
- [ ] `take_damage()` reduces health correctly
- [ ] Health never goes below 0
- [ ] `is_alive()` returns correct value
- [ ] `__str__` displays character status correctly
- [ ] Combat alternates turns correctly
- [ ] Combat ends when one character's health reaches 0
- [ ] Archer's dodge chance works (test multiple times)
- [ ] Archer's crit chance works (test multiple times)

## Stretch Goals (Optional)

- Add more character types (Rogue, Cleric, Paladin)
- Add special abilities (heal, shield, stun)
- Add inventory system (health potions, weapons)
- Add leveling system (gain XP, level up, increase stats)
- Add multiple rounds (best of 3)
- Add team battles (2v2)
- Save/load character data to file

## What This Demonstrates

This project demonstrates every major OOP concept:

1. **Abstraction:** `Character` is abstract, defines interface
2. **Inheritance:** Warrior/Mage/Archer inherit from `Character`
3. **Polymorphism:** All characters use same `attack()` interface
4. **Encapsulation:** `_health` is protected, accessed via methods
5. **Method Overriding:** Archer overrides `take_damage()` to add dodge
6. **`super()`:** All subclasses call `super().__init__()`
7. **Magic Methods:** `__str__` for readable output

## Why Do This Before Project 6?

Project 6 (IMS) is more complex and integrates concepts from all 4 weeks. If OOP feels shaky, this project:

- Is shorter (3-4 hours vs 8-12 hours)
- Is focused only on OOP (no file I/O, fewer edge cases)
- Is more fun (combat simulator vs inventory management)
- Demonstrates all OOP concepts you'll need for Project 6

**If RPG Arena feels easy, you're ready for Project 6.**  
**If RPG Arena feels challenging, spend time understanding it before moving on.**

## Submission

This project is optional and ungraded. You do not need to submit it. Use it as a learning tool.

## Need Help?

- Re-read Week 4 handbooks
- Run the demo code from sessions
- Compare your implementation to the provided structure above
- Attend office hours
