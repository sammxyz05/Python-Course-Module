"""
Demo: Abstract Base Classes
Shows: abc.ABC, @abstractmethod, enforcing interfaces
"""

from abc import ABC, abstractmethod

# Basic ABC example
print("=== Basic Abstract Base Class ===")

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def speak(self):
        """Subclasses must implement this."""
        pass

    @abstractmethod
    def move(self):
        """Subclasses must implement this."""
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Flying in the sky"

# This works
dog = Dog()
print(f"Dog speaks: {dog.speak()}")
print(f"Dog moves: {dog.move()}")

bird = Bird()
print(f"Bird speaks: {bird.speak()}")
print(f"Bird moves: {bird.move()}")

# This fails — Cat forgot to implement move()
print("\n=== Missing Implementation ===")

class Cat(Animal):
    def speak(self):
        return "Meow!"

    # ❌ Forgot to implement move()!

try:
    cat = Cat()  # Fails immediately
except TypeError as e:
    print(f"Error: {e}")


# Abstract method with default implementation
print("\n=== Abstract Method with Default ===")

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """Default implementation."""
        return "Starting vehicle..."

class Car(Vehicle):
    def start(self):
        # Can call parent's implementation
        base_message = super().start()
        return f"{base_message} Vroom!"

class Bicycle(Vehicle):
    def start(self):
        # Or provide completely new implementation
        return "Pedaling..."

car = Car()
bike = Bicycle()

print(car.start())
print(bike.start())


# Mixing abstract and concrete methods
print("\n=== Mixing Abstract and Concrete ===")

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, target):
        """Subclasses must implement."""
        pass

    @abstractmethod
    def special_ability(self, target):
        """Subclasses must implement."""
        pass

    def is_alive(self):
        """Concrete method — no need to override."""
        return self.health > 0

    def describe(self):
        """Concrete method."""
        status = "alive" if self.is_alive() else "defeated"
        return f"{self.name} (HP: {self.health}, {status})"

class Warrior(Character):
    def attack(self, target):
        return f"{self.name} swings sword at {target}"

    def special_ability(self, target):
        return f"{self.name} uses Shield Bash on {target}!"

class Mage(Character):
    def attack(self, target):
        return f"{self.name} casts magic missile at {target}"

    def special_ability(self, target):
        return f"{self.name} casts Fireball on {target}!"

warrior = Warrior("Conan", 100)
mage = Mage("Gandalf", 80)

print(warrior.describe())  # Uses inherited concrete method
print(warrior.attack("Goblin"))
print(warrior.special_ability("Goblin"))

print(mage.describe())
print(mage.attack("Dragon"))
print(mage.special_ability("Dragon"))


# Using ABCs to enforce interface
print("\n=== Enforcing Interface ===")

class Report(ABC):
    @abstractmethod
    def generate_header(self):
        pass

    @abstractmethod
    def generate_body(self):
        pass

    @abstractmethod
    def generate_footer(self):
        pass

    def generate(self):
        """Template method — calls abstract methods."""
        print(self.generate_header())
        print(self.generate_body())
        print(self.generate_footer())

class SalesReport(Report):
    def generate_header(self):
        return "=== SALES REPORT ==="

    def generate_body(self):
        return "Sales data: $100,000"

    def generate_footer(self):
        return "=== END REPORT ==="

report = SalesReport()
report.generate()


# Real-world example: payment methods
print("\n=== Real-World Example: Payment Methods ===")

class PaymentMethod(ABC):
    """Abstract interface for payment methods."""

    @abstractmethod
    def process_payment(self, amount):
        """Process a payment."""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund a payment."""
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Charged ${amount} to card ending in {self.card_number[-4:]}"

    def refund(self, amount):
        return f"Refunded ${amount} to card ending in {self.card_number[-4:]}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Charged ${amount} to PayPal account {self.email}"

    def refund(self, amount):
        return f"Refunded ${amount} to PayPal account {self.email}"

# Payment processing function works with any PaymentMethod
def checkout(payment_method: PaymentMethod, amount: float):
    """Process checkout with any payment method."""
    print(payment_method.process_payment(amount))

credit_card = CreditCard("1234-5678-9012-3456")
paypal = PayPal("user@example.com")

checkout(credit_card, 99.99)
checkout(paypal, 49.99)
