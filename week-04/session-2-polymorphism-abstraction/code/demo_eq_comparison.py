"""
Demo: __eq__ and Comparison Methods
Shows: implementing equality and rich comparison methods
"""

# Basic __eq__
print("=== Basic __eq__ ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """Two people are equal if they have the same name and age."""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f"{self.name} ({self.age})"

alice1 = Person("Alice", 30)
alice2 = Person("Alice", 30)
bob = Person("Bob", 25)

print(f"{alice1} == {alice2}: {alice1 == alice2}")  # True
print(f"{alice1} == {bob}: {alice1 == bob}")        # False
print(f"{alice1} != {bob}: {alice1 != bob}")        # True (automatically from __eq__)


# Without __eq__ (compares object identity)
print("\n=== Without __eq__ (compares identity) ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "Orwell")
book2 = Book("1984", "Orwell")

print(f"book1 == book2: {book1 == book2}")  # False — different objects
print(f"book1 is book2: {book1 is book2}")  # False — different objects
print(f"id(book1) == id(book2): {id(book1) == id(book2)}")  # False


# Rich comparison methods
print("\n=== Rich Comparison Methods ===")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        """Equal if same grade."""
        return self.grade == other.grade

    def __lt__(self, other):
        """Less than if lower grade."""
        return self.grade < other.grade

    def __le__(self, other):
        """Less than or equal."""
        return self.grade <= other.grade

    def __gt__(self, other):
        """Greater than if higher grade."""
        return self.grade > other.grade

    def __ge__(self, other):
        """Greater than or equal."""
        return self.grade >= other.grade

    def __str__(self):
        return f"{self.name} (grade: {self.grade})"

alice = Student("Alice", 95)
bob = Student("Bob", 85)
charlie = Student("Charlie", 95)

print(f"{alice} == {charlie}: {alice == charlie}")  # True
print(f"{alice} > {bob}: {alice > bob}")            # True
print(f"{bob} < {alice}: {bob < alice}")            # True
print(f"{alice} >= {charlie}: {alice >= charlie}")  # True


# Sorting with comparison methods
print("\n=== Sorting with Comparison Methods ===")

students = [
    Student("Alice", 95),
    Student("Bob", 85),
    Student("Charlie", 90),
    Student("Diana", 100)
]

sorted_students = sorted(students)
print("Students sorted by grade:")
for student in sorted_students:
    print(f"  {student}")


# Comparison with different types
print("\n=== Comparison with Different Types ===")

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        """Equal if same amount and currency."""
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        # Allow comparison with numbers (assume USD)
        if isinstance(other, (int, float)):
            return self.currency == "USD" and self.amount == other
        return False

    def __lt__(self, other):
        """Compare amounts (only if same currency)."""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot compare different currencies")
            return self.amount < other.amount
        if isinstance(other, (int, float)):
            if self.currency != "USD":
                raise ValueError("Can only compare with numbers in USD")
            return self.amount < other
        return NotImplemented

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

usd1 = Money(100, "USD")
usd2 = Money(50, "USD")
eur = Money(100, "EUR")

print(f"{usd1} == {usd2}: {usd1 == usd2}")  # False
print(f"{usd1} > {usd2}: {usd1 > usd2}")    # True
print(f"{usd1} == 100: {usd1 == 100}")      # True

try:
    print(f"{usd1} > {eur}: {usd1 > eur}")
except ValueError as e:
    print(f"Error: {e}")


# Complete example: Rectangle
print("\n=== Complete Example: Rectangle ===")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        """Rectangles are equal if same dimensions."""
        if not isinstance(other, Rectangle):
            return False
        return (self.width == other.width and self.height == other.height) or \
               (self.width == other.height and self.height == other.width)

    def __lt__(self, other):
        """Compare by area."""
        return self.area() < other.area()

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

rect1 = Rectangle(4, 5)
rect2 = Rectangle(5, 4)  # Same area, different dimensions
rect3 = Rectangle(3, 6)

print(f"{rect1} == {rect2}: {rect1 == rect2}")  # True (same dimensions, rotated)
print(f"{rect1} < {rect3}: {rect1 < rect3}")    # False (20 > 18)
print(f"{rect3} < {rect1}: {rect3 < rect1}")    # True (18 < 20)

rectangles = [rect1, rect2, rect3]
sorted_rects = sorted(rectangles)
print("\nRectangles sorted by area:")
for rect in sorted_rects:
    print(f"  {rect} (area: {rect.area()})")


# Using in sets and dicts (requires __eq__ and __hash__)
print("\n=== Using in Sets (requires __hash__) ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """Required for use in sets and as dict keys."""
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)  # Same coordinates
p3 = Point(3, 4)

# Without __hash__, points can't be added to sets
points = {p1, p2, p3}  # p1 and p2 are deduplicated
print(f"Unique points: {[str(p) for p in points]}")

# Can be used as dict keys
point_names = {p1: "Origin nearby", p3: "Far point"}
print(f"Name for {p2}: {point_names[p2]}")  # p2 has same hash as p1


# Summary
print("\n=== Summary ===")
print("""
Comparison methods:
  __eq__(self, other)  - equality (==)
  __ne__(self, other)  - inequality (!=) — auto-implemented from __eq__
  __lt__(self, other)  - less than (<)
  __le__(self, other)  - less than or equal (<=)
  __gt__(self, other)  - greater than (>)
  __ge__(self, other)  - greater than or equal (>=)

Tips:
  - Always check isinstance(other, YourClass) in __eq__
  - Return False if comparison doesn't make sense
  - Return NotImplemented for unsupported types
  - Implement __hash__ if you implement __eq__ and want to use in sets/dicts
  - __hash__ should return the same value for objects that are __eq__
""")
