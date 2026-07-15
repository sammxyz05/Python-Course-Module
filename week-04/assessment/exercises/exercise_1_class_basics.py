"""
Exercise 1: Class Basics
Practice: defining classes, __init__, instance attributes, methods, magic methods
"""


# TODO 1: Create a Person class
# Requirements:
# - __init__ takes name and age
# - Store name and age as instance attributes
# - Method greet() returns "Hello, my name is {name} and I am {age} years old."
# - Implement __str__ to return "{name} ({age})"

class Person:
    pass  # Replace with your code


# TODO 2: Create a BankAccount class
# Requirements:
# - __init__ takes account_holder (str) and balance (float, default 0.0)
# - Method deposit(amount) adds amount to balance, returns new balance
# - Method withdraw(amount) subtracts amount from balance, returns new balance
# - Method get_balance() returns current balance
# - Implement __str__ to return "Account: {holder}, Balance: ${balance:.2f}"

class BankAccount:
    pass  # Replace with your code


# TODO 3: Create a Rectangle class
# Requirements:
# - __init__ takes width and height
# - Method area() returns width * height
# - Method perimeter() returns 2 * (width + height)
# - Method is_square() returns True if width == height, else False
# - Implement __str__ to return "Rectangle({width}x{height})"
# - Implement __repr__ to return "Rectangle(width={width}, height={height})"

class Rectangle:
    pass  # Replace with your code


# TODO 4: Create a Book class with validation
# Requirements:
# - __init__ takes title, author, pages
# - Validate: title and author must be non-empty strings
# - Validate: pages must be positive integer
# - Raise ValueError if validation fails
# - Method info() returns "{title} by {author} ({pages} pages)"
# - Implement __str__ to return the same as info()

class Book:
    pass  # Replace with your code


# TODO 5: Create a Counter class
# Requirements:
# - __init__ initializes count to 0
# - Method increment() increases count by 1
# - Method decrement() decreases count by 1 (but not below 0)
# - Method reset() sets count back to 0
# - Method get_count() returns current count
# - Implement __str__ to return "Count: {count}"

class Counter:
    pass  # Replace with your code


# Test your classes (uncomment to test)
if __name__ == "__main__":
    # Test TODO 1: Person
    # person = Person("Alice", 30)
    # print(person.greet())  # Expected: Hello, my name is Alice and I am 30 years old.
    # print(person)  # Expected: Alice (30)

    # Test TODO 2: BankAccount
    # account = BankAccount("Bob", 1000.0)
    # print(account)  # Expected: Account: Bob, Balance: $1000.00
    # account.deposit(500)
    # print(account.get_balance())  # Expected: 1500.0
    # account.withdraw(200)
    # print(account.get_balance())  # Expected: 1300.0

    # Test TODO 3: Rectangle
    # rect = Rectangle(5, 10)
    # print(rect.area())  # Expected: 50
    # print(rect.perimeter())  # Expected: 30
    # print(rect.is_square())  # Expected: False
    # print(rect)  # Expected: Rectangle(5x10)
    # print(repr(rect))  # Expected: Rectangle(width=5, height=10)

    # square = Rectangle(4, 4)
    # print(square.is_square())  # Expected: True

    # Test TODO 4: Book
    # try:
    #     book = Book("1984", "George Orwell", 328)
    #     print(book.info())  # Expected: 1984 by George Orwell (328 pages)
    #     print(book)  # Expected: 1984 by George Orwell (328 pages)
    # except ValueError as e:
    #     print(f"Error: {e}")

    # try:
    #     bad_book = Book("", "Author", 100)  # Should raise ValueError
    # except ValueError as e:
    #     print(f"Caught error: {e}")  # Expected: Caught error: ...

    # try:
    #     bad_book = Book("Title", "Author", -10)  # Should raise ValueError
    # except ValueError as e:
    #     print(f"Caught error: {e}")  # Expected: Caught error: ...

    # Test TODO 5: Counter
    # counter = Counter()
    # print(counter)  # Expected: Count: 0
    # counter.increment()
    # counter.increment()
    # print(counter.get_count())  # Expected: 2
    # counter.decrement()
    # print(counter.get_count())  # Expected: 1
    # counter.decrement()
    # counter.decrement()  # Should not go below 0
    # print(counter.get_count())  # Expected: 0
    # counter.increment()
    # counter.increment()
    # counter.reset()
    # print(counter.get_count())  # Expected: 0

    pass
