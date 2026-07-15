# Session 2 — Polymorphism, Abstraction, and Magic Methods

**Duration:** 90 minutes

## Overview

This session completes your OOP foundation with the final two pillars (polymorphism and abstraction) plus Python's magic methods. These concepts let you write elegant, reusable code that feels like it's part of Python itself.

This session covers:
- **Polymorphism:** Same interface, different implementations (method overriding, duck typing)
- **Abstraction:** Abstract Base Classes (ABCs) with `@abstractmethod`
- **Magic methods:** `__str__`, `__repr__`, `__eq__`, `__add__`, and more

By the end of this session, you'll understand how Python's built-in types (`list`, `dict`, `str`) work under the hood and how to make your own classes behave like them.

## Handbooks

Read these in order:

1. **[01-polymorphism.md](./01-polymorphism.md)**
   - What polymorphism means
   - Method overriding (subclass replaces parent's method)
   - Duck typing ("if it walks like a duck...")
   - When to use polymorphism

2. **[02-abstraction-abc.md](./02-abstraction-abc.md)**
   - Abstract Base Classes (ABCs)
   - The `abc` module
   - `@abstractmethod` decorator
   - Enforcing interfaces
   - When to use abstraction

3. **[03-magic-methods.md](./03-magic-methods.md)**
   - What are magic methods (dunder methods)
   - `__str__` and `__repr__` for string representation
   - `__eq__`, `__lt__`, etc. for comparisons
   - `__add__`, `__sub__`, etc. for operators
   - `__len__`, `__getitem__`, etc. for container behavior

## Code Demos

All demo files are runnable:

- **[`demo_polymorphism.py`](./code/demo_polymorphism.py)** — Method overriding and duck typing examples
- **[`demo_abstract_base_class.py`](./code/demo_abstract_base_class.py)** — Using `abc.ABC` and `@abstractmethod`
- **[`demo_shape_circle_square.py`](./code/demo_shape_circle_square.py)** — The live-coded example from class: Shape ABC with Circle and Square subclasses
- **[`demo_magic_methods.py`](./code/demo_magic_methods.py)** — Overview of common magic methods
- **[`demo_str_repr.py`](./code/demo_str_repr.py)** — `__str__` vs `__repr__` explained
- **[`demo_eq_comparison.py`](./code/demo_eq_comparison.py)** — Implementing `__eq__` and other comparison methods
- **[`demo_point_class.py`](./code/demo_point_class.py)** — The live-coded example from class: Point class with `__str__`, `__eq__`, and `__add__`

## Key Takeaways

- **Polymorphism lets different classes share the same interface.** A `Dog` and a `Cat` can both `speak()`, but the implementation differs.
- **Duck typing:** Python doesn't care about the type, only that the object has the right methods. "If it walks like a duck and quacks like a duck, it's a duck."
- **Abstract Base Classes enforce contracts.** Use `abc.ABC` and `@abstractmethod` to define interfaces that subclasses must implement.
- **Magic methods make your classes feel like built-in types.** Implement `__str__` for readable output, `__eq__` for comparisons, `__add__` for `+`, etc.
- **`__str__` vs `__repr__`:** `__str__` is for end users (readable), `__repr__` is for developers (unambiguous, ideally `eval()`-able).

## Final Project Reminder

After this session, you have all the tools for Project 5 (RPG Arena) and Project 6 (IMS). 

**If OOP still feels unclear, DO PROJECT 5 FIRST.** It's explicitly designed as extra practice. Better to spend Saturday on RPG Arena and Sunday–Wednesday on IMS than to jump straight into IMS while shaky on inheritance and polymorphism.

## What's Next

The weekend assessment begins. You have two projects:
- **Project 5: RPG Arena (OPTIONAL)** — Ungraded extra practice, highly recommended if OOP is still fuzzy
- **Project 6: Inventory & Invoice Management System (MANDATORY)** — The final assessment, integrates everything from Weeks 1–4

There is **NO in-class review** of Project 6. You are responsible for integrating all concepts.
