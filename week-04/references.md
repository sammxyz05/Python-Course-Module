# Week 4 References — Official Python Documentation

This page links to the authoritative sources for every concept covered in Week 4. When OOP doesn't make sense, start here.

## Classes and Objects

- **Classes** — [python.org/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
  - Class definition, `__init__`, `self`, instance vs class attributes
- **Class and Instance Variables** — [python.org/tutorial/classes.html#class-and-instance-variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
  - When to use class attributes vs instance attributes
- **Method Objects** — [python.org/tutorial/classes.html#method-objects](https://docs.python.org/3/tutorial/classes.html#method-objects)
  - How `self` works, method binding

## Inheritance

- **Inheritance** — [python.org/tutorial/classes.html#inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
  - Single inheritance, `super()`, method overriding
- **Multiple Inheritance** — [python.org/tutorial/classes.html#multiple-inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
  - MRO (Method Resolution Order), diamond problem
- **super() Built-in** — [python.org/library/functions.html#super](https://docs.python.org/3/library/functions.html#super)
  - Calling parent class methods

## Encapsulation

- **Private Variables** — [python.org/tutorial/classes.html#private-variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
  - Name mangling with `__`, convention with `_`
- **Property Decorator** — [python.org/library/functions.html#property](https://docs.python.org/3/library/functions.html#property)
  - Pythonic getters and setters

## Polymorphism and Abstraction

- **Abstract Base Classes (abc)** — [python.org/library/abc.html](https://docs.python.org/3/library/abc.html)
  - `ABC`, `@abstractmethod`, enforcing interfaces
- **Duck Typing** — [docs.python.org/3/glossary.html#term-duck-typing](https://docs.python.org/3/glossary.html#term-duck-typing)
  - "If it walks like a duck and quacks like a duck..."

## Magic Methods (Dunder Methods)

- **Data Model (Special Method Names)** — [python.org/reference/datamodel.html#special-method-names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
  - Complete list of all magic methods
- **Object Representation** — `__repr__`, `__str__`
  - [python.org/reference/datamodel.html#object.__repr__](https://docs.python.org/3/reference/datamodel.html#object.__repr__)
  - [python.org/reference/datamodel.html#object.__str__](https://docs.python.org/3/reference/datamodel.html#object.__str__)
- **Rich Comparison Methods** — `__eq__`, `__lt__`, `__le__`, etc.
  - [python.org/reference/datamodel.html#object.__eq__](https://docs.python.org/3/reference/datamodel.html#object.__eq__)
- **Emulating Numeric Types** — `__add__`, `__sub__`, `__mul__`, etc.
  - [python.org/reference/datamodel.html#emulating-numeric-types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
- **Emulating Container Types** — `__len__`, `__getitem__`, `__setitem__`
  - [python.org/reference/datamodel.html#emulating-container-types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)

## Style and Best Practices

- **PEP 8 — Naming Conventions** — [peps.python.org/pep-0008/#naming-conventions](https://peps.python.org/pep-0008/#naming-conventions)
  - Class names (PascalCase), method names (lowercase_with_underscores)
- **Composition vs Inheritance** — [python-patterns.guide/gang-of-four/composition-over-inheritance](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
  - When to use "has-a" instead of "is-a"

## Additional Resources

- **Real Python: OOP in Python 3** — [realpython.com/python3-object-oriented-programming](https://realpython.com/python3-object-oriented-programming/)
- **Real Python: Inheritance and Composition** — [realpython.com/inheritance-composition-python](https://realpython.com/inheritance-composition-python/)
- **Real Python: Python's super()** — [realpython.com/python-super](https://realpython.com/python-super/)
- **Corey Schafer: OOP Tutorial Series** — [youtube.com/watch?v=ZDa-Z5JzLYM](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
