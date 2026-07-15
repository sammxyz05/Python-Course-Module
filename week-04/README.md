# Week 4 — Object-Oriented Programming (OOP)

## Why this week matters

This is the **final week** and the **hardest conceptual jump** in the course. **Object-Oriented Programming** lets you model real-world entities as objects with attributes (data) and methods (behavior). By Friday you will understand classes, inheritance, polymorphism, and abstraction—the four pillars of OOP.

⚠️ **Week 4 compresses 4 OOP pillars + magic methods into 2 sessions.** The final project (IMS) integrates OOP with ALL prior concepts (functions, file I/O, exceptions) for the first time. There is **NO in-class review** of the final project—it is the terminal assessment.

⚠️ **If OOP feels unclear after Session 2, DO PROJECT 5 (RPG ARENA) FIRST.** It is explicitly designed as extra practice. Better to spend Saturday on RPG and Sunday–Wed on IMS than to jump straight into IMS while shaky on inheritance.

## Objectives — by Friday night you should be able to:

- Define classes with `__init__`, instance attributes, and methods
- Understand and apply encapsulation (public vs private attributes)
- Use inheritance to create subclasses that extend base classes
- Call parent methods with `super()`
- Implement polymorphism through method overriding
- Create abstract base classes (ABCs) with abstract methods
- Implement magic methods (`__str__`, `__eq__`, `__repr__`)

## Sessions

| Session | Date | Covers | Handbook |
|---|---|---|---|
| Session 1 (Thu) | **30-min Review: Cart Engine + Log Analyzer** → Classes, Inheritance, Encapsulation | Review anonymized Week 3 bugs, then: class definition, `__init__`, `self`, instance vs class attributes, encapsulation (`_` and `__`), inheritance, `super()`, method overriding | [`session-1-classes-and-inheritance/`](./session-1-classes-and-inheritance/) |
| Session 2 (Fri) | Polymorphism, Abstraction, Magic Methods | Polymorphism via method overriding, duck typing, Abstract Base Classes (abc module), `@abstractmethod`, magic methods (`__str__`, `__repr__`, `__eq__`, `__add__`, etc.) | [`session-2-polymorphism-abstraction/`](./session-2-polymorphism-abstraction/) |

## Weekend assessment

Once both sessions are done, work through **[`assessment/README.md`](./assessment/README.md)** — Saturday through Wednesday. 

The projects this week are:
- **Project 5: RPG Arena (OPTIONAL)** — turn-based combat, demonstrates all OOP concepts, ungraded extra practice
- **Project 6: Inventory & Invoice Management System (MANDATORY)** — the final assessment, integrates OOP + functions + file I/O + exceptions

**Project 6 (IMS) is the sole final assessment.** There is NO in-class review. You are responsible for integrating everything from Weeks 1-4.

## The Four Pillars of OOP

1. **Encapsulation** — Hide internal state, expose controlled interface
2. **Abstraction** — Hide complexity, show only essentials
3. **Inheritance** — Reuse code by deriving from base classes
4. **Polymorphism** — Same interface, different implementations

You will use all four pillars in the final project.

## Further reading

See **[`references.md`](./references.md)** for the official docs that back every concept taught this week.
