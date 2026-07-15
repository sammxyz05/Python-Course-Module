"""
Demo: Point Class (live-coded example)
Shows: Complete class with __str__, __eq__, __add__, and more
This is the exact example from the master schedule and class lecture.
"""

class Point:
    """Represents a point in 2D space."""

    def __init__(self, x, y):
        """Initialize point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """User-friendly string representation."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Developer-friendly representation (eval-able)."""
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """Check if two points are equal."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Add two points."""
        if not isinstance(other, Point):
            raise TypeError(f"Cannot add Point and {type(other).__name__}")
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two points."""
        if not isinstance(other, Point):
            raise TypeError(f"Cannot subtract Point and {type(other).__name__}")
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply point by scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Cannot multiply Point by {type(scalar).__name__}")
        return Point(self.x * scalar, self.y * scalar)

    def __hash__(self):
        """Make point hashable (for use in sets and as dict keys)."""
        return hash((self.x, self.y))

    def distance_from_origin(self):
        """Calculate distance from origin (0, 0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, other):
        """Calculate distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# Create points
print("=== Creating Points ===")
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(1, 2)  # Same as p1

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")


# String representations
print("\n=== String Representations ===")
print(f"str(p1): {str(p1)}")
print(f"repr(p1): {repr(p1)}")
print(f"print(p1): {p1}")

# In a list, repr is used
print(f"Points list: {[p1, p2, p3]}")


# Equality
print("\n=== Equality ===")
print(f"p1 == p2: {p1 == p2}")  # False
print(f"p1 == p3: {p1 == p3}")  # True
print(f"p1 != p2: {p1 != p2}")  # True


# Arithmetic operations
print("\n=== Arithmetic Operations ===")
print(f"p1 + p2 = {p1 + p2}")      # (4, 6)
print(f"p2 - p1 = {p2 - p1}")      # (2, 2)
print(f"p1 * 3 = {p1 * 3}")        # (3, 6)


# Distance calculations
print("\n=== Distance Calculations ===")
print(f"p1 distance from origin: {p1.distance_from_origin():.2f}")
print(f"p2 distance from origin: {p2.distance_from_origin():.2f}")
print(f"Distance from p1 to p2: {p1.distance_to(p2):.2f}")


# Using points in sets (requires __hash__ and __eq__)
print("\n=== Using Points in Sets ===")
points = {p1, p2, p3}  # p1 and p3 are deduplicated
print(f"Unique points: {points}")
print(f"Number of unique points: {len(points)}")


# Using points as dict keys
print("\n=== Using Points as Dict Keys ===")
locations = {
    Point(0, 0): "Origin",
    Point(1, 0): "East",
    Point(0, 1): "North",
    Point(-1, 0): "West",
    Point(0, -1): "South"
}

origin = Point(0, 0)
print(f"Location at {origin}: {locations[origin]}")


# Vector operations
print("\n=== Vector Operations ===")

def midpoint(p1, p2):
    """Calculate midpoint between two points."""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

def translate(point, dx, dy):
    """Translate point by dx and dy."""
    return point + Point(dx, dy)

mid = midpoint(p1, p2)
print(f"Midpoint between {p1} and {p2}: {mid}")

translated = translate(p1, 5, 3)
print(f"{p1} translated by (5, 3): {translated}")


# Chaining operations
print("\n=== Chaining Operations ===")
result = (p1 + p2) * 2 - Point(1, 1)
print(f"(p1 + p2) * 2 - (1, 1) = {result}")


# Error handling
print("\n=== Error Handling ===")
try:
    p1 + "hello"
except TypeError as e:
    print(f"Error: {e}")

try:
    p1 * Point(2, 3)
except TypeError as e:
    print(f"Error: {e}")


# Using with sorted (needs __lt__ for default sorting)
print("\n=== Sorting Points ===")

# Add __lt__ temporarily for this example
class SortablePoint(Point):
    def __lt__(self, other):
        """Sort by distance from origin."""
        return self.distance_from_origin() < other.distance_from_origin()

points_to_sort = [
    SortablePoint(5, 0),
    SortablePoint(1, 1),
    SortablePoint(3, 4),
    SortablePoint(0, 2)
]

sorted_points = sorted(points_to_sort)
print("Points sorted by distance from origin:")
for point in sorted_points:
    print(f"  {point} (distance: {point.distance_from_origin():.2f})")


# Complete usage example
print("\n=== Complete Usage Example ===")

class Shape:
    """A shape defined by multiple points."""

    def __init__(self, points):
        self.points = points

    def center(self):
        """Calculate center point (centroid)."""
        avg_x = sum(p.x for p in self.points) / len(self.points)
        avg_y = sum(p.y for p in self.points) / len(self.points)
        return Point(avg_x, avg_y)

    def translate(self, dx, dy):
        """Translate all points."""
        return Shape([p + Point(dx, dy) for p in self.points])

# Create a triangle
triangle = Shape([
    Point(0, 0),
    Point(4, 0),
    Point(2, 3)
])

print(f"Triangle points: {triangle.points}")
print(f"Triangle center: {triangle.center()}")

# Move triangle
moved = triangle.translate(5, 5)
print(f"Moved triangle points: {moved.points}")
print(f"Moved triangle center: {moved.center()}")


# Summary
print("\n=== Summary ===")
print("""
Point class demonstrates:
  - __init__: Initialize with x, y coordinates
  - __str__: User-friendly output "(x, y)"
  - __repr__: Developer output "Point(x, y)"
  - __eq__: Check equality
  - __add__: Add two points
  - __sub__: Subtract two points
  - __mul__: Multiply by scalar
  - __hash__: Enable use in sets and as dict keys
  - distance_from_origin(): Calculate distance
  - distance_to(other): Calculate distance to another point

This is a complete, Pythonic class!
""")
