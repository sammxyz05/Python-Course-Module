# Project 6: Inventory & Invoice Management System (IMS)

## ⚠️ CRITICAL: Final Assessment

This is your **mandatory final project** for the Python bootcamp. It is the **sole basis** for your final grade.

- **Due:** Wednesday night
- **No extensions**
- **No in-class review**
- **Start Saturday, not Sunday night**

---

## What This Project Tests

This project integrates concepts from **all 4 weeks**:

| Week | Concepts | Application in IMS |
|------|----------|-------------------|
| **Week 1** | Variables, loops, conditionals, data structures | Main menu loop, user input validation, storing products/invoices |
| **Week 2** | Lists, dicts, tuples, sets | Product lists, invoice items (list of dicts), product info (dicts) |
| **Week 3** | Functions, file I/O, exceptions | Modular functions, JSON save/load, error handling |
| **Week 4** | OOP (classes, inheritance, polymorphism) | Product hierarchy, Invoice class, polymorphic product types |

---

## Project Overview

Build a console-based system to manage:
1. **Products** (perishable and non-perishable)
2. **Invoices** (with items, tax, totals)
3. **File persistence** (save/load data)

### Class Hierarchy

```
Product (base)
├── PerishableProduct (expiry date)
└── NonPerishableProduct (warranty)

Invoice (invoice items, tax, totals)

InvoiceManager (manages multiple invoices)
```

---

## Getting Started

### Step 1: Read the Spec

**READ THIS FIRST:** [`PROJECT_SPEC.md`](./PROJECT_SPEC.md)

The spec contains:
- Detailed requirements
- Complete class specifications with code examples
- User flow diagrams
- Implementation guide (step-by-step)
- Testing checklist

**Do not skip the spec.** It has everything you need.

### Step 2: Start with `ims_starter.py`

The starter file has:
- TODO comments for all 17 tasks
- Skeleton classes and functions
- Test cases (commented out)
- Suggested structure

### Step 3: Build Incrementally

**Don't write everything at once.** Follow this order:

1. **Product classes** (TODO 1-3)
   - Implement `Product` base class
   - Test it (uncomment test cases)
   - Implement `PerishableProduct`
   - Test it
   - Implement `NonPerishableProduct`
   - Test it

2. **Invoice classes** (TODO 4-5)
   - Implement `Invoice` class
   - Test it
   - Implement `InvoiceManager`
   - Test it

3. **User interface** (TODO 6-16)
   - Implement product management functions
   - Test each function
   - Implement invoice management functions
   - Test each function
   - Implement save/load functions
   - Test them

4. **Main loop** (TODO 17)
   - Connect all pieces
   - Test full workflow

### Step 4: Test Thoroughly

See **Testing Checklist** in `PROJECT_SPEC.md`.

Test:
- All features work
- Edge cases (empty inputs, negative values, missing files)
- Error handling (invalid inputs, file errors)
- File save/load roundtrip

---

## Timeline Recommendation

**Total: 8-12 hours**

| Day | Tasks | Hours |
|-----|-------|-------|
| **Saturday** | Read spec, implement Product classes (TODO 1-3) | 3-4 hours |
| **Sunday** | Implement Invoice classes (TODO 4-5), start UI functions (TODO 6-10) | 3-4 hours |
| **Monday** | Finish UI functions (TODO 11-16), implement main loop (TODO 17) | 2-3 hours |
| **Tuesday** | Test everything, fix bugs, handle edge cases | 2-3 hours |
| **Wednesday** | Final testing, polish, submit | 1-2 hours |

**If you start Sunday night, you will not finish on time.**

---

## Common Pitfalls

1. **Not reading the spec**
   - The spec has complete code examples
   - Don't guess what to do—read the spec

2. **Not testing incrementally**
   - Don't write 500 lines then test
   - Write one class, test it, move on

3. **Forgetting `super().__init__()`**
   - This is the #1 OOP mistake
   - See [`../../common_mistakes.md`](../../common_mistakes.md)

4. **Not handling exceptions**
   - Wrap user inputs in try/except
   - Handle FileNotFoundError, ValueError, etc.

5. **Not validating inputs**
   - Check for empty strings, negative numbers
   - Raise ValueError with helpful messages

---

## If OOP Feels Unclear

⚠️ **Do Project 5 (RPG Arena) first:**
- It's shorter (3-4 hours)
- Demonstrates all OOP concepts you need
- Is more fun (combat simulator)
- Is optional and ungraded

**Only do Project 5 if OOP feels shaky.** If you're confident, go straight to Project 6.

---

## Grading Criteria

See [`../../final_project_rubric.md`](../../final_project_rubric.md) for complete rubric.

**Summary (100 points total):**
- **Functionality (40 pts):** All features work correctly
- **OOP Design (30 pts):** Proper use of classes, inheritance, polymorphism
- **Integration (20 pts):** Combines concepts from all 4 weeks
- **Code Quality (10 pts):** Readable, documented, tested

**Automatic deductions:**
- Late submission: -10 pts per day
- Code doesn't run: -20 pts
- Missing required classes: -15 pts
- No file I/O: -10 pts
- No exception handling: -10 pts

---

## Submission Checklist

Before submitting, verify:

- [ ] All TODO tasks completed (17 total)
- [ ] All classes implemented (Product, PerishableProduct, NonPerishableProduct, Invoice, InvoiceManager)
- [ ] All features work (product management, invoice management, file I/O)
- [ ] Edge cases handled (empty inputs, negative values, missing files)
- [ ] Exceptions handled (ValueError, FileNotFoundError, json.JSONDecodeError)
- [ ] Code runs without syntax errors
- [ ] Code is documented (docstrings, comments)
- [ ] Reflection log completed ([`../../reflection_log.md`](../../reflection_log.md))
- [ ] This README updated with your notes (optional but recommended)

---

## Need Help?

If you get stuck:

1. **Re-read the spec:** It has code examples for every class
2. **Check common mistakes:** [`../../common_mistakes.md`](../../common_mistakes.md)
3. **Review handbooks:** Week 4 sessions
4. **Run demo code:** Modify session demos
5. **Do Project 5 first:** If OOP is unclear
6. **Office hours:** Check syllabus for schedule
7. **Ask classmates:** Discuss concepts, not code

**Don't stay stuck for more than 30 minutes.** Get help.

---

## Sample Output

```
========================================
    Inventory & Invoice Manager
========================================
1. Product Management
2. Invoice Management
3. Save/Load Data
4. Exit

Choose an option: 1

--- Product Management ---
1. Add Product
2. Update Product
3. Remove Product
4. Display All Products
5. Search Product
6. Back to Main Menu

Choose an option: 1

Add Product Type:
1. Perishable
2. Non-Perishable

Choose type: 1

Enter product name: Milk
Enter product ID: P001
Enter price: 4.99
Enter quantity: 50
Enter expiry date (YYYY-MM-DD): 2026-07-20

✓ Product added successfully!

Milk (ID: P001): $4.99 [Stock: 50] [Expires: 2026-07-20]
```

---

## After Submission

After you submit:

1. Complete the reflection log (if you haven't already)
2. Review instructor feedback
3. Keep this code as a portfolio piece
4. Be proud—you built a real system integrating 4 weeks of concepts!

---

## Final Reminders

⚠️ **This is your final assessment. There is no safety net.**

- Start Saturday
- Test thoroughly
- Handle edge cases
- Document your code
- Ask for help if stuck

**You've learned everything you need. This project proves you can put it all together.**

**Good luck! You've got this!**
