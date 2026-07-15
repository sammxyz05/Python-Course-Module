"""
Demo: Shape, Circle, Square (live-coded example)
Shows: ABC with abstract methods, concrete implementations
This is the exact example from the master schedule and class lecture.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Calculate area. Subclasses must implement."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter. Subclasses must implement."""
        pass

    def describe(self):
        """Concrete method — all shapes can use this."""
        return f"{self.__class__.__name__} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    """Circle implements Shape interface."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Implement abstract method."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Implement abstract method."""
        return 2 * math.pi * self.radius


class Square(Shape):
    """Square implements Shape interface."""

    def __init__(self, side):
        self.side = side

    def area(self):
        """Implement abstract method."""
        return self.side ** 2

    def perimeter(self):
        """Implement abstract method."""
        return 4 * self.side


# Create shapes
print("=== Creating shapes ===")
circle = Circle(5)
square = Square(4)

# Calculate area and perimeter
print(f"\nCircle (radius={circle.radius}):")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

print(f"\nSquare (side={square.side}):")
print(f"  Area: {square.area():.2f}")
print(f"  Perimeter: {square.perimeter():.2f}")

# Use describe method (inherited from Shape)
print("\n=== Using describe method ===")
print(circle.describe())
print(square.describe())


# Polymorphism — function works with any Shape
print("\n=== Polymorphic Function ===")

def print_shape_info(shape: Shape):
    """Works with any Shape subclass."""
    print(shape.describe())

print_shape_info(circle)
print_shape_info(square)


# Collection of shapes
print("\n=== Collection of Shapes ===")

shapes = [
    Circle(3),
    Square(5),
    Circle(7),
    Square(2)
]

total_area = sum(shape.area() for shape in shapes)
print(f"Total area of all shapes: {total_area:.2f}")

for i, shape in enumerate(shapes, 1):
    print(f"Shape {i}: {shape.describe()}")


# Extending the hierarchy
print("\n=== Extending with Rectangle ===")

class Rectangle(Shape):
    """Rectangle implements Shape interface."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(6, 3)
print(rect.describe())


# Demonstrating that incomplete subclasses fail
print("\n=== Incomplete Subclass (will fail) ===")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    # ❌ Forgot to implement perimeter()!

try:
    triangle = Triangle(4, 3)
except TypeError as e:
    print(f"Error creating Triangle: {e}")


# Complete implementation with all methods
print("\n=== Complete Triangle Implementation ===")

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

triangle = Triangle(3, 4, 5)
print(triangle.describe())


# Type checking
print("\n=== Type Checking ===")
print(f"circle is a Circle: {isinstance(circle, Circle)}")
print(f"circle is a Shape: {isinstance(circle, Shape)}")
print(f"square is a Square: {isinstance(square, Square)}")
print(f"square is a Shape: {isinstance(square, Shape)}")
print(f"Circle is subclass of Shape: {issubclass(Circle, Shape)}")
print(f"Square is subclass of Shape: {issubclass(Square, Shape)}")
