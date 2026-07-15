"""
Exercise 3: Polymorphism and Magic Methods
Practice: polymorphism, magic methods (__str__, __repr__, __eq__, __lt__, __len__, etc.)
"""


# TODO 1: Create Payment classes demonstrating polymorphism
# Create three classes: CashPayment, CreditCardPayment, MobilePayment
# Each must have:
# - __init__ with appropriate parameters (amount for all, plus card_number for credit, app_name for mobile)
# - process() method that returns different messages
# - __str__ method
#
# Requirements:
# - CashPayment.process() returns "Processing cash payment of ${amount:.2f}"
# - CreditCardPayment.process() returns "Processing credit card payment of ${amount:.2f} (Card: ****{last_4_digits})"
# - MobilePayment.process() returns "Processing mobile payment of ${amount:.2f} via {app_name}"
#
# Then write a function process_payments(payments: list) that takes a list of payment objects
# and calls process() on each one (demonstrating polymorphism)

class CashPayment:
    pass  # Replace with your code


class CreditCardPayment:
    pass  # Replace with your code


class MobilePayment:
    pass  # Replace with your code


def process_payments(payments):
    """Process a list of payments polymorphically."""
    pass  # Replace with your code


# TODO 2: Create Product class with comparison magic methods
# Requirements:
# - __init__ takes name, price, and rating (1-5)
# - Implement __str__ to return "{name}: ${price:.2f} (Rating: {rating}/5)"
# - Implement __repr__ to return "Product(name={name!r}, price={price}, rating={rating})"
# - Implement __eq__ to compare by name (case-insensitive)
# - Implement __lt__ to compare by price (for sorting)
# - Implement __hash__ to hash by name.lower() (so products can be used in sets/dicts)

class Product:
    pass  # Replace with your code


# TODO 3: Create Playlist class with container magic methods
# Requirements:
# - __init__ takes name and initializes empty list of songs
# - Method add_song(song_name) adds a song to the list
# - Method remove_song(song_name) removes a song from the list
# - Implement __len__ to return number of songs
# - Implement __getitem__ to support indexing (playlist[0])
# - Implement __contains__ to support 'in' operator ("song" in playlist)
# - Implement __str__ to return "Playlist '{name}' with {count} songs"

class Playlist:
    pass  # Replace with your code


# TODO 4: Create Vector2D class with arithmetic magic methods
# Requirements:
# - __init__ takes x and y coordinates
# - Implement __str__ to return "Vector({x}, {y})"
# - Implement __repr__ to return "Vector2D(x={x}, y={y})"
# - Implement __eq__ to compare vectors by x and y
# - Implement __add__ to add two vectors (returns new Vector2D)
# - Implement __sub__ to subtract two vectors (returns new Vector2D)
# - Implement __mul__ to multiply vector by scalar (returns new Vector2D)
# - Method magnitude() returns sqrt(x^2 + y^2)

class Vector2D:
    pass  # Replace with your code


# TODO 5: Create Temperature class with conversion magic methods
# Requirements:
# - __init__ takes temperature in Celsius
# - Method to_fahrenheit() returns temperature in Fahrenheit: (celsius * 9/5) + 32
# - Method to_kelvin() returns temperature in Kelvin: celsius + 273.15
# - Implement __str__ to return "{celsius}°C"
# - Implement __repr__ to return "Temperature(celsius={celsius})"
# - Implement __eq__ to compare temperatures (in Celsius)
# - Implement __lt__ to compare temperatures (in Celsius)
# - Implement __format__ to support format strings:
#   - format(temp, 'C') returns "{celsius}°C"
#   - format(temp, 'F') returns "{fahrenheit}°F"
#   - format(temp, 'K') returns "{kelvin}K"

class Temperature:
    pass  # Replace with your code


# Test your classes (uncomment to test)
if __name__ == "__main__":
    # Test TODO 1: Payment polymorphism
    # cash = CashPayment(50.0)
    # credit = CreditCardPayment(100.0, "1234567890123456")
    # mobile = MobilePayment(75.0, "PayApp")
    #
    # print(cash.process())  # Expected: Processing cash payment of $50.00
    # print(credit.process())  # Expected: Processing credit card payment of $100.00 (Card: ****3456)
    # print(mobile.process())  # Expected: Processing mobile payment of $75.00 via PayApp
    #
    # payments = [cash, credit, mobile]
    # process_payments(payments)  # Should call process() on each

    # Test TODO 2: Product comparison
    # p1 = Product("Laptop", 999.99, 4)
    # p2 = Product("Mouse", 25.99, 5)
    # p3 = Product("Laptop", 899.99, 4)  # Same name, different price
    #
    # print(p1)  # Expected: Laptop: $999.99 (Rating: 4/5)
    # print(repr(p2))  # Expected: Product(name='Mouse', price=25.99, rating=5)
    #
    # print(p1 == p3)  # Expected: True (same name)
    # print(p1 < p2)  # Expected: False (999.99 > 25.99)
    #
    # products = [p1, p2, p3]
    # products.sort()  # Sort by price using __lt__
    # print([str(p) for p in products])  # Expected: Mouse first, then laptops
    #
    # product_set = {p1, p2, p3}  # Should work because of __hash__
    # print(len(product_set))  # Expected: 2 (p1 and p3 have same hash)

    # Test TODO 3: Playlist container
    # playlist = Playlist("My Favorites")
    # playlist.add_song("Song A")
    # playlist.add_song("Song B")
    # playlist.add_song("Song C")
    #
    # print(playlist)  # Expected: Playlist 'My Favorites' with 3 songs
    # print(len(playlist))  # Expected: 3
    # print(playlist[0])  # Expected: Song A
    # print("Song B" in playlist)  # Expected: True
    # print("Song Z" in playlist)  # Expected: False
    #
    # playlist.remove_song("Song B")
    # print(len(playlist))  # Expected: 2

    # Test TODO 4: Vector2D arithmetic
    # v1 = Vector2D(3, 4)
    # v2 = Vector2D(1, 2)
    #
    # print(v1)  # Expected: Vector(3, 4)
    # print(repr(v2))  # Expected: Vector2D(x=1, y=2)
    #
    # v3 = v1 + v2
    # print(v3)  # Expected: Vector(4, 6)
    #
    # v4 = v1 - v2
    # print(v4)  # Expected: Vector(2, 2)
    #
    # v5 = v1 * 2
    # print(v5)  # Expected: Vector(6, 8)
    #
    # print(f"Magnitude of v1: {v1.magnitude():.2f}")  # Expected: 5.00

    # Test TODO 5: Temperature conversion and formatting
    # temp = Temperature(25)
    # print(temp)  # Expected: 25°C
    # print(repr(temp))  # Expected: Temperature(celsius=25)
    # print(f"Fahrenheit: {temp.to_fahrenheit()}")  # Expected: Fahrenheit: 77.0
    # print(f"Kelvin: {temp.to_kelvin()}")  # Expected: Kelvin: 298.15
    #
    # print(format(temp, 'C'))  # Expected: 25°C
    # print(format(temp, 'F'))  # Expected: 77.0°F
    # print(format(temp, 'K'))  # Expected: 298.15K
    #
    # temp1 = Temperature(20)
    # temp2 = Temperature(30)
    # print(temp1 == temp2)  # Expected: False
    # print(temp1 < temp2)  # Expected: True

    pass
