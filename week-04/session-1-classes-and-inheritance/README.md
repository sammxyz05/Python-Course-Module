# Session 1 — Classes and Inheritance

**Duration:** 90 minutes (30 min review + 60 min new content)

## Overview

This is the gateway session to Object-Oriented Programming. OOP is the **hardest conceptual jump** in the course—you're moving from procedural code (functions + data structures) to modeling real-world entities as objects with both data (attributes) and behavior (methods).

This session covers:
- **30-minute review:** Anonymized bugs from Week 3's Cart Engine and Log Analyzer projects
- **Classes and objects:** `class`, `__init__`, `self`, instances
- **Attributes:** instance attributes vs class attributes
- **Encapsulation:** public vs private (`_` and `__` conventions)
- **Inheritance:** base classes, subclasses, `super()`, method overriding

## Handbooks

Read these in order:

1. **[01-classes-instances-attributes.md](./01-classes-instances-attributes.md)**
   - Class definition syntax
   - The `__init__` constructor
   - `self` explained
   - Instance vs class attributes
   - Methods vs functions

2. **[02-encapsulation.md](./02-encapsulation.md)**
   - Public attributes (normal names)
   - Protected attributes (`_single_underscore`)
   - Private attributes (`__double_underscore`)
   - Name mangling
   - Getters and setters with `@property`

3. **[03-inheritance.md](./03-inheritance.md)**
   - Base class and subclass syntax
   - `super()` to call parent methods
   - Method overriding
   - When to use inheritance

## Code Demos

All demo files are runnable. Type them out yourself, experiment with modifications:

- **[`demo_class_basics.py`](./code/demo_class_basics.py)** — Simple class with `__init__`, attributes, and methods
- **[`demo_instance_vs_class_attributes.py`](./code/demo_instance_vs_class_attributes.py)** — The difference between instance and class attributes
- **[`demo_encapsulation.py`](./code/demo_encapsulation.py)** — Public, protected, and private attributes
- **[`demo_getters_setters.py`](./code/demo_getters_setters.py)** — Using `@property` for controlled access
- **[`demo_inheritance.py`](./code/demo_inheritance.py)** — Base class and subclass with `super()`
- **[`demo_animal_dog.py`](./code/demo_animal_dog.py)** — The live-coded example from class: Animal with private `__sound` attribute, Dog subclass

## Key Takeaways

- **Classes are blueprints, instances are objects.** A `Car` class defines what all cars have; `my_car = Car()` creates one specific car.
- **`__init__` is the constructor.** It runs when you create an instance: `obj = MyClass()` calls `__init__(self)`.
- **`self` is the instance.** When you call `obj.method()`, Python rewrites it to `MyClass.method(obj)`. `self` is how the method knows which instance it's working on.
- **Instance attributes are per-object.** Each instance has its own `.name`, `.age`, etc.
- **Class attributes are shared.** All instances see the same class attribute unless they override it.
- **Encapsulation hides internals.** Use `_protected` for internal-use attributes and `__private` for name-mangled attributes that subclasses shouldn't touch.
- **Inheritance models "is-a" relationships.** `Dog` is an `Animal`, so `Dog` inherits from `Animal`.
- **`super()` calls parent methods.** Use it in `__init__` to initialize the parent part of the object.

## What's Next

Session 2 covers polymorphism (same method, different behavior), abstraction (abstract base classes), and magic methods (`__str__`, `__eq__`, etc.)—the final OOP concepts you need for the projects.
