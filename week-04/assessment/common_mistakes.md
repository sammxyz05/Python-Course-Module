# Common Mistakes — Week 4 (OOP)

These are anonymized bugs from previous cohorts. Read this *before* starting your projects.

## Classes and Instances

### Forgetting `self` Parameter

```python
# ❌ WRONG: missing self parameter
class Product:
    def __init__(name, price):  # TypeError: takes 2 positional arguments but 3 were given
        self.name = name

# ✅ CORRECT: self is always first parameter
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

### Forgetting `self.` When Accessing Instance Attributes

```python
# ❌ WRONG: accessing attributes without self
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        print(name)  # NameError: name 'name' is not defined

# ✅ CORRECT: use self.attribute_name
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        print(self.name)  # Access via self
```

### Calling Methods Without `self.`

```python
# ❌ WRONG: calling method without self
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add_ten(self, num):
        return add(num, 10)  # NameError: name 'add' is not defined

# ✅ CORRECT: call methods with self.
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add_ten(self, num):
        return self.add(num, 10)  # Call via self
```

### Confusing Class vs Instance Attributes

```python
# ❌ WRONG: class attribute is shared across all instances
class Product:
    quantity = 0  # Class attribute (shared by ALL instances)
    
    def __init__(self, name):
        self.name = name
        quantity = 5  # Local variable, not an attribute!

# ✅ CORRECT: instance attributes are per-instance
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity  # Instance attribute (unique per instance)
```

## Inheritance

### Not Calling `super().__init__()`

```python
# ❌ WRONG: parent's __init__ is not called
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PerishableProduct(Product):
    def __init__(self, name, price, expiry_date):
        # Missing super().__init__()!
        self.expiry_date = expiry_date  # name and price are never set!

# ✅ CORRECT: call parent's __init__
class PerishableProduct(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)  # Initialize parent attributes
        self.expiry_date = expiry_date
```

### Calling Parent Method Incorrectly

```python
# ❌ WRONG: calling parent method directly on class
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        base_sound = Animal.speak()  # TypeError: missing 1 required positional argument: 'self'
        return base_sound + " Woof!"

# ✅ CORRECT: use super() or pass self explicitly
class Dog(Animal):
    def speak(self):
        base_sound = super().speak()  # Correct way
        return base_sound + " Woof!"

# ✅ ALTERNATIVE: pass self explicitly (less common)
class Dog(Animal):
    def speak(self):
        base_sound = Animal.speak(self)  # Works but super() is preferred
        return base_sound + " Woof!"
```

### Overriding `__init__` Without Preserving Parent's Initialization

```python
# ❌ WRONG: completely replaces parent's __init__
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self._generate_id()

class PerishableProduct(Product):
    def __init__(self, expiry_date):
        self.expiry_date = expiry_date  # name, price, id are never set!

# ✅ CORRECT: call parent's __init__ first
class PerishableProduct(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)  # Preserves parent's initialization
        self.expiry_date = expiry_date
```

## Abstract Base Classes (ABC)

### Trying to Instantiate Abstract Class

```python
from abc import ABC, abstractmethod

# ❌ WRONG: trying to create instance of abstract class
class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

player = Character()  # TypeError: Can't instantiate abstract class Character

# ✅ CORRECT: only instantiate concrete subclasses
class Warrior(Character):
    def attack(self):
        return "Swings sword"

player = Warrior()  # This works
```

### Forgetting to Implement Abstract Method

```python
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

# ❌ WRONG: subclass doesn't implement attack()
class Mage(Character):
    def cast_spell(self):
        return "Casts fireball"

wizard = Mage()  # TypeError: Can't instantiate abstract class Mage

# ✅ CORRECT: implement all abstract methods
class Mage(Character):
    def attack(self):
        return "Casts fireball"

wizard = Mage()  # This works
```

### Wrong Abstract Method Decorator Import

```python
# ❌ WRONG: importing from wrong module
from abc import abstractmethod  # Missing ABC!

class Character(abstractmethod):  # Wrong! abstractmethod is not a class
    pass

# ✅ CORRECT: import both ABC and abstractmethod
from abc import ABC, abstractmethod

class Character(ABC):  # Inherit from ABC
    @abstractmethod  # Use as decorator
    def attack(self):
        pass
```

## Polymorphism

### Expecting Same Method Signature Across Polymorphic Classes

```python
# ❌ WRONG: different signatures break polymorphism
class Warrior:
    def attack(self, target):
        return f"Attacks {target}"

class Mage:
    def attack(self, target, spell):  # Different signature!
        return f"Casts {spell} on {target}"

# This breaks when used polymorphically:
characters = [Warrior(), Mage()]
for char in characters:
    print(char.attack("enemy"))  # TypeError for Mage: missing required argument 'spell'

# ✅ CORRECT: consistent signatures
class Warrior:
    def attack(self, target):
        return f"Attacks {target}"

class Mage:
    def attack(self, target):
        return f"Casts fireball on {target}"
```

### Not Returning Consistent Types

```python
# ❌ WRONG: one returns string, another returns int
class Product:
    def get_description(self):
        return "Generic product"

class PerishableProduct(Product):
    def get_description(self):
        return 42  # Different type!

# ✅ CORRECT: return same type
class PerishableProduct(Product):
    def get_description(self):
        return "Perishable product with expiry date"
```

## Magic Methods

### Implementing `__eq__` But Forgetting `__hash__`

```python
# ❌ WRONG: implementing __eq__ makes object unhashable
class Product:
    def __init__(self, product_id):
        self.product_id = product_id
    
    def __eq__(self, other):
        return self.product_id == other.product_id

p1 = Product(1)
products = {p1}  # TypeError: unhashable type: 'Product'

# ✅ CORRECT: implement both __eq__ and __hash__
class Product:
    def __init__(self, product_id):
        self.product_id = product_id
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.product_id == other.product_id
    
    def __hash__(self):
        return hash(self.product_id)
```

### Wrong `__str__` Return Type

```python
# ❌ WRONG: __str__ must return string
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return (self.name, self.price)  # Returns tuple!

print(Product("Apple", 1.5))  # TypeError: __str__ returned non-string

# ✅ CORRECT: always return string
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"
```

### Confusing `__str__` vs `__repr__`

```python
# ❌ WRONG: using __repr__ for user-facing output
class Product:
    def __repr__(self):
        return f"Product: {self.name}"  # This is for developers, not users

# ✅ CORRECT: __str__ for users, __repr__ for debugging
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"  # User-friendly
    
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"  # Developer-friendly
```

## Encapsulation

### Directly Accessing Private Attributes from Outside

```python
# ❌ WRONG: accessing private attribute (name mangling)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (name mangled)

account = BankAccount(1000)
print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# ✅ CORRECT: use getter method
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Correct
```

### Exposing Mutable Attributes Without Protection

```python
# ❌ WRONG: returning mutable attribute directly
class Invoice:
    def __init__(self):
        self._items = []
    
    def get_items(self):
        return self._items  # Returns direct reference!

invoice = Invoice()
items = invoice.get_items()
items.append("hacked")  # Modifies internal state!

# ✅ CORRECT: return a copy
class Invoice:
    def __init__(self):
        self._items = []
    
    def get_items(self):
        return self._items.copy()  # Returns copy
```

## Project-Specific: IMS

### Not Validating Input in `__init__`

```python
# ❌ WRONG: accepting invalid data
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # What if price is negative?

# ✅ CORRECT: validate in constructor
class Product:
    def __init__(self, name, price):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        
        self.name = name
        self.price = price
```

### Forgetting to Handle File I/O Exceptions

```python
# ❌ WRONG: no exception handling
class InvoiceManager:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.data)  # What if disk is full? Permission denied?

# ✅ CORRECT: handle exceptions
class InvoiceManager:
    def save_to_file(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(self.data)
            print(f"Saved to {filename}")
        except PermissionError:
            print(f"Permission denied: {filename}")
        except IOError as e:
            print(f"I/O error: {e}")
```

### Not Overriding `__str__` for Display

```python
# ❌ WRONG: printing object without __str__
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

print(Product("Apple", 1.5))  # <__main__.Product object at 0x...>

# ✅ CORRECT: implement __str__ for readable output
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

print(Product("Apple", 1.5))  # Apple: $1.50
```

### Circular Dependencies Between Classes

```python
# ❌ WRONG: Invoice creates InvoiceManager, InvoiceManager creates Invoice
class Invoice:
    def __init__(self):
        self.manager = InvoiceManager()  # Circular!

class InvoiceManager:
    def __init__(self):
        self.invoices = [Invoice()]  # Circular!

# ✅ CORRECT: clear dependency direction
class Invoice:
    def __init__(self):
        self.items = []

class InvoiceManager:
    def __init__(self):
        self.invoices = []  # Manager owns invoices, not vice versa
    
    def create_invoice(self):
        return Invoice()
```

## General

### Not Testing Edge Cases

Test these before submitting:

- Empty inputs (empty name, zero price)
- Negative numbers (price, quantity)
- Missing files (FileNotFoundError)
- Malformed file data (JSON parse errors)
- Invalid types (passing string where int expected)
- Large inputs (1000+ products)

### Not Using Type Hints (Optional But Recommended)

```python
# ❌ WRONG: no type hints (harder to debug)
def add_product(product):
    pass

# ✅ CORRECT: type hints clarify intent
def add_product(self, product: Product) -> None:
    pass
```

### Overcomplicating Inheritance

```python
# ❌ WRONG: too many inheritance levels
class Entity:
    pass

class Item(Entity):
    pass

class Product(Item):
    pass

class PerishableProduct(Product):
    pass

# ✅ CORRECT: keep it simple
class Product:
    pass

class PerishableProduct(Product):
    pass
```

## How to Avoid These

1. **Read the handbooks carefully** — every mistake listed here is covered
2. **Run demo code** — modify it, break it, fix it
3. **Test incrementally** — write one method, test it, move on
4. **Use print statements** — see what your attributes contain
5. **Read error messages** — Python tells you exactly what went wrong
6. **Do Project 5 (RPG Arena) first** — it demonstrates all concepts in a simpler form
