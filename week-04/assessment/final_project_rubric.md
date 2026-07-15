# Final Project Grading Rubric — Project 6 (IMS)

## Overview

This rubric is used to grade **Project 6: Inventory & Invoice Management System**, the sole final assessment for the bootcamp.

**Total Points: 100**

---

## 1. Functionality (40 points)

Does the program work as specified?

### Core Features (30 points)

- **Product Management (10 points)**
  - Add product (base, perishable, non-perishable): 3 pts
  - Update product (name, price, quantity): 3 pts
  - Remove product: 2 pts
  - Display all products: 2 pts

- **Invoice Management (10 points)**
  - Create invoice: 2 pts
  - Add items to invoice: 3 pts
  - Calculate invoice total (including tax): 3 pts
  - Display invoice details: 2 pts

- **File I/O (10 points)**
  - Save products to file: 3 pts
  - Load products from file: 3 pts
  - Save invoices to file: 2 pts
  - Load invoices from file: 2 pts

### Edge Case Handling (10 points)

- Empty inputs (empty product name, zero price): 2 pts
- Negative values (price, quantity): 2 pts
- Missing files (FileNotFoundError): 2 pts
- Malformed file data (JSON parse errors): 2 pts
- Invalid operations (remove non-existent product): 2 pts

---

## 2. OOP Design (30 points)

Is OOP used correctly and effectively?

### Class Design (12 points)

- **Product base class** (4 pts)
  - Proper `__init__` with validation: 1 pt
  - Instance attributes (name, price, quantity): 1 pt
  - Methods (update, display): 1 pt
  - Magic methods (`__str__`, `__repr__`): 1 pt

- **PerishableProduct and NonPerishableProduct subclasses** (4 pts)
  - Inherits from Product: 1 pt
  - Calls `super().__init__()`: 1 pt
  - Adds subclass-specific attributes: 1 pt
  - Overrides methods appropriately: 1 pt

- **Invoice class** (2 pts)
  - Manages list of items: 1 pt
  - Calculates total correctly: 1 pt

- **InvoiceManager class** (2 pts)
  - Manages list of invoices: 1 pt
  - Provides CRUD operations: 1 pt

### Inheritance (6 points)

- Uses `super()` correctly in subclasses: 2 pts
- Method overriding is appropriate: 2 pts
- Inheritance hierarchy makes sense: 2 pts

### Polymorphism (6 points)

- Subclasses can be used interchangeably via base class interface: 3 pts
- Polymorphic behavior is demonstrated (e.g., different display formats): 3 pts

### Encapsulation (6 points)

- Attributes are private/protected where appropriate: 2 pts
- Public interface is clean and minimal: 2 pts
- Internal implementation is hidden: 2 pts

---

## 3. Integration (20 points)

Does the project integrate concepts from all 4 weeks?

### Week 1: Fundamentals (5 points)

- Uses loops appropriately: 2 pts
- Uses conditionals for logic: 2 pts
- Uses data structures (lists, dicts): 1 pt

### Week 2: Data Structures (5 points)

- Uses lists for collections: 2 pts
- Uses dicts for structured data: 2 pts
- Uses appropriate data structure methods: 1 pt

### Week 3: Functions, File I/O, Exceptions (5 points)

- Reusable helper functions: 2 pts
- File I/O with `with` statement: 2 pts
- Exception handling (try/except): 1 pt

### Week 4: OOP (5 points)

- Classes and inheritance: 2 pts
- Polymorphism: 2 pts
- Magic methods: 1 pt

---

## 4. Code Quality (10 points)

Is the code readable, maintainable, and well-organized?

### Naming and Style (3 points)

- Variable/function/class names are descriptive: 1 pt
- Follows Python naming conventions (snake_case, PascalCase): 1 pt
- Code is properly indented and formatted: 1 pt

### Documentation (3 points)

- Docstrings for classes: 1 pt
- Docstrings for methods: 1 pt
- Inline comments for complex logic: 1 pt

### Organization (2 points)

- Code is organized into logical sections: 1 pt
- Functions/methods are single-purpose: 1 pt

### Testing (2 points)

- Code has been tested with sample data: 1 pt
- Edge cases have been tested: 1 pt

---

## Grade Breakdown

| Points | Grade | Description |
|--------|-------|-------------|
| 90-100 | A     | Exceptional work. All features work correctly, OOP design is excellent, integration is seamless, code quality is professional. |
| 80-89  | B     | Strong work. Most features work, OOP design is solid, integration is good, minor code quality issues. |
| 70-79  | C     | Adequate work. Core features work, OOP design is functional, integration is present, code quality needs improvement. |
| 60-69  | D     | Needs improvement. Some features work, OOP design has issues, integration is incomplete, code quality is poor. |
| 0-59   | F     | Unsatisfactory. Major features don't work, OOP design is incorrect, integration is missing, code quality is unacceptable. |

---

## Automatic Deductions

- **Late submission:** -10 points per day
- **Code doesn't run:** -20 points (fix syntax errors before submitting!)
- **Missing required classes:** -15 points
- **No file I/O:** -10 points
- **No exception handling:** -10 points
- **Plagiarism:** 0 points + academic integrity violation

---

## What Graders Look For

### Excellent Projects (A)

- All features work flawlessly
- OOP design is elegant and appropriate
- Integration is seamless—concepts from all weeks work together naturally
- Code is clean, readable, and well-documented
- Edge cases are handled gracefully
- Code demonstrates deep understanding of OOP principles

### Good Projects (B)

- Most features work correctly
- OOP design is solid with minor issues
- Integration is present but could be smoother
- Code is readable with some documentation
- Some edge cases are handled
- Code demonstrates good understanding of OOP principles

### Adequate Projects (C)

- Core features work
- OOP design is functional but not optimal
- Integration is present but basic
- Code is somewhat readable
- Few edge cases are handled
- Code demonstrates basic understanding of OOP principles

### Projects That Need Improvement (D/F)

- Features don't work or are incomplete
- OOP design is incorrect or missing
- Integration is missing or broken
- Code is hard to read or poorly organized
- Edge cases are not handled
- Code demonstrates misunderstanding of OOP principles

---

## Self-Check Before Submission

Use this checklist to review your project:

- [ ] All classes are implemented (Product, PerishableProduct, NonPerishableProduct, Invoice, InvoiceManager)
- [ ] All methods work as specified
- [ ] `super().__init__()` is called in subclasses
- [ ] Magic methods (`__str__`, `__repr__`) are implemented
- [ ] File I/O uses `with` statement
- [ ] Exceptions are handled (FileNotFoundError, ValueError, etc.)
- [ ] Code runs without syntax errors
- [ ] Edge cases are tested (empty inputs, negative values, missing files)
- [ ] Code is documented (docstrings, comments)
- [ ] Variable/class names follow conventions
- [ ] README.md is included with usage instructions
- [ ] Reflection log is completed

---

## Questions?

If you're unsure whether your implementation meets the rubric criteria:

1. Re-read the project spec
2. Review the common mistakes guide
3. Compare your code to the demo code from sessions
4. Attend office hours

**Remember:** This is your final assessment. Start early, test thoroughly, ask for help if stuck.
