"""
Exercise 2: Inheritance Practice
Practice: inheritance, super(), method overriding, extending parent classes
"""


# TODO 1: Create Vehicle base class and Car subclass
# Vehicle requirements:
# - __init__ takes brand and model
# - Method start() returns "{brand} {model} is starting..."
# - Implement __str__ to return "{brand} {model}"
#
# Car requirements (inherits from Vehicle):
# - __init__ takes brand, model, and num_doors
# - Call super().__init__() for brand and model
# - Store num_doors as instance attribute
# - Override __str__ to return "{brand} {model} ({num_doors} doors)"

class Vehicle:
    pass  # Replace with your code


class Car(Vehicle):
    pass  # Replace with your code


# TODO 2: Create Animal base class and Dog subclass
# Animal requirements:
# - __init__ takes name
# - Method speak() returns "Some sound"
# - Method info() returns "I am {name}"
#
# Dog requirements (inherits from Animal):
# - __init__ takes name and breed
# - Call super().__init__() for name
# - Store breed as instance attribute
# - Override speak() to return "Woof!"
# - Override info() to return "I am {name}, a {breed}"

class Animal:
    pass  # Replace with your code


class Dog(Animal):
    pass  # Replace with your code


# TODO 3: Create Employee base class and Manager subclass
# Employee requirements:
# - __init__ takes name and salary
# - Method get_details() returns "{name}: ${salary}"
# - Method give_raise(amount) increases salary by amount
#
# Manager requirements (inherits from Employee):
# - __init__ takes name, salary, and department
# - Call super().__init__() for name and salary
# - Store department as instance attribute
# - Override get_details() to include department: "{name} (Manager - {department}): ${salary}"
# - Add method manage() that returns "{name} is managing the {department} department"

class Employee:
    pass  # Replace with your code


class Manager(Employee):
    pass  # Replace with your code


# TODO 4: Create Shape base class with Circle and Square subclasses
# Shape requirements:
# - __init__ takes name (str)
# - Method area() raises NotImplementedError with message "Subclass must implement area()"
# - Method perimeter() raises NotImplementedError with message "Subclass must implement perimeter()"
#
# Circle requirements (inherits from Shape):
# - __init__ takes radius
# - Call super().__init__("Circle")
# - Override area() to return π * radius^2 (use 3.14159 for π)
# - Override perimeter() to return 2 * π * radius
#
# Square requirements (inherits from Shape):
# - __init__ takes side
# - Call super().__init__("Square")
# - Override area() to return side^2
# - Override perimeter() to return 4 * side

class Shape:
    pass  # Replace with your code


class Circle(Shape):
    pass  # Replace with your code


class Square(Shape):
    pass  # Replace with your code


# TODO 5: Create Account base class with SavingsAccount and CheckingAccount subclasses
# Account requirements:
# - __init__ takes account_number and balance (default 0.0)
# - Method deposit(amount) adds to balance, returns new balance
# - Method withdraw(amount) subtracts from balance, returns new balance
# - Method get_balance() returns balance
# - Implement __str__ to return "Account {account_number}: ${balance:.2f}"
#
# SavingsAccount requirements (inherits from Account):
# - __init__ takes account_number, balance (default 0.0), and interest_rate (default 0.01)
# - Call super().__init__() for account_number and balance
# - Store interest_rate as instance attribute
# - Add method add_interest() that increases balance by balance * interest_rate
# - Override __str__ to return "Savings Account {account_number}: ${balance:.2f} ({interest_rate*100}% interest)"
#
# CheckingAccount requirements (inherits from Account):
# - __init__ takes account_number, balance (default 0.0), and overdraft_limit (default 100.0)
# - Call super().__init__() for account_number and balance
# - Store overdraft_limit as instance attribute
# - Override withdraw() to allow negative balance up to -overdraft_limit
# - If withdrawal exceeds overdraft_limit, raise ValueError("Overdraft limit exceeded")
# - Override __str__ to return "Checking Account {account_number}: ${balance:.2f} (overdraft: ${overdraft_limit})"

class Account:
    pass  # Replace with your code


class SavingsAccount(Account):
    pass  # Replace with your code


class CheckingAccount(Account):
    pass  # Replace with your code


# Test your classes (uncomment to test)
if __name__ == "__main__":
    # Test TODO 1: Vehicle and Car
    # vehicle = Vehicle("Generic", "Model")
    # print(vehicle.start())  # Expected: Generic Model is starting...
    # print(vehicle)  # Expected: Generic Model

    # car = Car("Toyota", "Camry", 4)
    # print(car.start())  # Expected: Toyota Camry is starting...
    # print(car)  # Expected: Toyota Camry (4 doors)

    # Test TODO 2: Animal and Dog
    # animal = Animal("Generic Animal")
    # print(animal.speak())  # Expected: Some sound
    # print(animal.info())  # Expected: I am Generic Animal

    # dog = Dog("Buddy", "Golden Retriever")
    # print(dog.speak())  # Expected: Woof!
    # print(dog.info())  # Expected: I am Buddy, a Golden Retriever

    # Test TODO 3: Employee and Manager
    # employee = Employee("Alice", 50000)
    # print(employee.get_details())  # Expected: Alice: $50000
    # employee.give_raise(5000)
    # print(employee.get_details())  # Expected: Alice: $55000

    # manager = Manager("Bob", 80000, "Engineering")
    # print(manager.get_details())  # Expected: Bob (Manager - Engineering): $80000
    # print(manager.manage())  # Expected: Bob is managing the Engineering department
    # manager.give_raise(10000)
    # print(manager.get_details())  # Expected: Bob (Manager - Engineering): $90000

    # Test TODO 4: Shape, Circle, and Square
    # circle = Circle(5)
    # print(f"Circle area: {circle.area():.2f}")  # Expected: Circle area: 78.54
    # print(f"Circle perimeter: {circle.perimeter():.2f}")  # Expected: Circle perimeter: 31.42

    # square = Square(4)
    # print(f"Square area: {square.area()}")  # Expected: Square area: 16
    # print(f"Square perimeter: {square.perimeter()}")  # Expected: Square perimeter: 16

    # Test TODO 5: Account, SavingsAccount, and CheckingAccount
    # savings = SavingsAccount("SA001", 1000.0, 0.05)
    # print(savings)  # Expected: Savings Account SA001: $1000.00 (5.0% interest)
    # savings.add_interest()
    # print(savings)  # Expected: Savings Account SA001: $1050.00 (5.0% interest)

    # checking = CheckingAccount("CA001", 500.0, 200.0)
    # print(checking)  # Expected: Checking Account CA001: $500.00 (overdraft: $200.0)
    # checking.withdraw(600)
    # print(checking.get_balance())  # Expected: -100.0
    # try:
    #     checking.withdraw(200)  # Should raise ValueError
    # except ValueError as e:
    #     print(f"Error: {e}")  # Expected: Error: Overdraft limit exceeded

    pass
