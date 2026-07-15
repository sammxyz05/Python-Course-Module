# Project 6: Inventory & Invoice Management System (IMS)

## ⚠️ CRITICAL: This is Your Final Assessment

This project is **MANDATORY** and is your **sole final assessment** for the bootcamp.

- **No in-class review:** You will not present this project
- **Due:** Wednesday night
- **No extensions**
- **Integrates all 4 weeks:** OOP + functions + file I/O + exceptions + data structures

**Start Saturday. Test thoroughly. Ask for help if stuck.**

---

## Overview

Build a console-based Inventory & Invoice Management System for a small business. The system manages products (perishable and non-perishable), creates invoices, calculates totals with tax, and persists data to files.

This project demonstrates your mastery of:
- **Week 1:** Variables, loops, conditionals, data structures
- **Week 2:** Lists, dicts, tuples, sets
- **Week 3:** Functions, file I/O, exceptions
- **Week 4:** OOP (classes, inheritance, polymorphism, abstraction)

**Estimated time:** 8-12 hours  
**Due:** Wednesday night  
**Grading:** See [`../../final_project_rubric.md`](../../final_project_rubric.md)

---

## Learning Objectives

- Design a class hierarchy using inheritance
- Implement polymorphism across product types
- Use encapsulation to protect data
- Integrate file I/O for persistence
- Handle exceptions gracefully
- Create a cohesive system from multiple components

---

## Requirements

### Core Features (Required)

Your IMS must support:

#### 1. Product Management
- Add products (base, perishable, non-perishable)
- Update product details (name, price, quantity)
- Remove products
- Display all products (formatted, readable)
- Search products by name or ID

#### 2. Invoice Management
- Create new invoice
- Add products to invoice
- Remove products from invoice
- Calculate invoice total (subtotal + tax)
- Display invoice details (items, quantities, prices, total)
- List all invoices

#### 3. File Persistence
- Save products to JSON file
- Load products from JSON file
- Save invoices to JSON file
- Load invoices from JSON file
- Handle missing/corrupted files gracefully

#### 4. Error Handling
- Validate all user inputs (name, price, quantity, etc.)
- Handle FileNotFoundError for missing files
- Handle ValueError for invalid data types
- Handle JSON parsing errors for corrupted files
- Provide helpful error messages

---

## Class Design

### Class Hierarchy Diagram

```
                    Product (base class)
                    ├── name: str
                    ├── product_id: str
                    ├── price: float
                    ├── quantity: int
                    ├── __init__(name, product_id, price, quantity)
                    ├── update_price(new_price)
                    ├── update_quantity(new_quantity)
                    ├── get_info() -> dict
                    ├── __str__() -> str
                    └── __repr__() -> str
                           │
        ┌──────────────────┴──────────────────┐
        │                                      │
PerishableProduct                    NonPerishableProduct
├── expiry_date: str                 ├── warranty_years: int
├── __init__(name, id, price,        ├── __init__(name, id, price,
│     qty, expiry_date)              │     qty, warranty_years)
├── is_expired() -> bool             ├── has_warranty() -> bool
├── days_until_expiry() -> int       ├── get_info() -> dict (override)
├── get_info() -> dict (override)    ├── __str__() -> str (override)
└── __str__() -> str (override)      └── __repr__() -> str (override)



                    Invoice
                    ├── invoice_id: str
                    ├── items: list[dict]
                    ├── tax_rate: float
                    ├── __init__(invoice_id, tax_rate=0.08)
                    ├── add_item(product, quantity)
                    ├── remove_item(product_id)
                    ├── calculate_subtotal() -> float
                    ├── calculate_tax() -> float
                    ├── calculate_total() -> float
                    ├── get_items() -> list[dict]
                    ├── __str__() -> str
                    └── __repr__() -> str



                    InvoiceManager
                    ├── invoices: list[Invoice]
                    ├── __init__()
                    ├── create_invoice(invoice_id, tax_rate) -> Invoice
                    ├── get_invoice(invoice_id) -> Invoice
                    ├── list_invoices() -> list[Invoice]
                    ├── save_to_file(filename)
                    ├── load_from_file(filename)
                    └── __str__() -> str
```

---

## Detailed Class Specifications

### 1. Product (Base Class)

```python
class Product:
    """Base class for all products."""

    def __init__(self, name, product_id, price, quantity):
        """
        Initialize product.

        Args:
            name (str): Product name
            product_id (str): Unique product ID
            price (float): Product price (must be >= 0)
            quantity (int): Stock quantity (must be >= 0)

        Raises:
            ValueError: If validation fails
        """
        # Validate inputs
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")

        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        """Update product price."""
        if not isinstance(new_price, (int, float)) or new_price < 0:
            raise ValueError("Price must be a non-negative number")
        self.price = new_price

    def update_quantity(self, new_quantity):
        """Update product quantity."""
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.quantity = new_quantity

    def get_info(self):
        """
        Return product info as dictionary.

        Returns:
            dict: Product information
        """
        return {
            "name": self.name,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "type": "Product"
        }

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name} (ID: {self.product_id}): ${self.price:.2f} [Stock: {self.quantity}]"

    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Product(name={self.name!r}, product_id={self.product_id!r}, price={self.price}, quantity={self.quantity})"
```

### 2. PerishableProduct (Subclass)

```python
from datetime import datetime, timedelta

class PerishableProduct(Product):
    """Perishable product with expiry date."""

    def __init__(self, name, product_id, price, quantity, expiry_date):
        """
        Initialize perishable product.

        Args:
            name (str): Product name
            product_id (str): Unique product ID
            price (float): Product price
            quantity (int): Stock quantity
            expiry_date (str): Expiry date in format "YYYY-MM-DD"

        Raises:
            ValueError: If validation fails
        """
        super().__init__(name, product_id, price, quantity)

        # Validate expiry_date format
        try:
            datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Expiry date must be in format YYYY-MM-DD")

        self.expiry_date = expiry_date

    def is_expired(self):
        """Check if product is expired."""
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        return datetime.now() > expiry

    def days_until_expiry(self):
        """Return days until expiry (negative if expired)."""
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        delta = expiry - datetime.now()
        return delta.days

    def get_info(self):
        """Return product info with expiry date."""
        info = super().get_info()
        info["expiry_date"] = self.expiry_date
        info["type"] = "PerishableProduct"
        return info

    def __str__(self):
        """User-friendly string representation."""
        base_str = super().__str__()
        status = "EXPIRED" if self.is_expired() else f"Expires: {self.expiry_date}"
        return f"{base_str} [{status}]"
```

### 3. NonPerishableProduct (Subclass)

```python
class NonPerishableProduct(Product):
    """Non-perishable product with warranty."""

    def __init__(self, name, product_id, price, quantity, warranty_years):
        """
        Initialize non-perishable product.

        Args:
            name (str): Product name
            product_id (str): Unique product ID
            price (float): Product price
            quantity (int): Stock quantity
            warranty_years (int): Warranty duration in years

        Raises:
            ValueError: If validation fails
        """
        super().__init__(name, product_id, price, quantity)

        if not isinstance(warranty_years, int) or warranty_years < 0:
            raise ValueError("Warranty years must be a non-negative integer")

        self.warranty_years = warranty_years

    def has_warranty(self):
        """Check if product has warranty."""
        return self.warranty_years > 0

    def get_info(self):
        """Return product info with warranty."""
        info = super().get_info()
        info["warranty_years"] = self.warranty_years
        info["type"] = "NonPerishableProduct"
        return info

    def __str__(self):
        """User-friendly string representation."""
        base_str = super().__str__()
        warranty_str = f"{self.warranty_years} year warranty" if self.has_warranty() else "No warranty"
        return f"{base_str} [{warranty_str}]"
```

### 4. Invoice

```python
class Invoice:
    """Invoice containing multiple product items."""

    def __init__(self, invoice_id, tax_rate=0.08):
        """
        Initialize invoice.

        Args:
            invoice_id (str): Unique invoice ID
            tax_rate (float): Tax rate (default 8%)
        """
        self.invoice_id = invoice_id
        self.tax_rate = tax_rate
        self._items = []  # List of dicts: {"product": Product, "quantity": int}

    def add_item(self, product, quantity):
        """
        Add product to invoice.

        Args:
            product (Product): Product instance
            quantity (int): Quantity to add

        Raises:
            ValueError: If quantity invalid or exceeds stock
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if quantity > product.quantity:
            raise ValueError(f"Insufficient stock. Available: {product.quantity}")

        # Check if product already in invoice
        for item in self._items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                return

        # Add new item
        self._items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_id):
        """Remove item from invoice by product ID."""
        self._items = [item for item in self._items if item["product"].product_id != product_id]

    def calculate_subtotal(self):
        """Calculate subtotal (before tax)."""
        return sum(item["product"].price * item["quantity"] for item in self._items)

    def calculate_tax(self):
        """Calculate tax amount."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        """Calculate total (subtotal + tax)."""
        return self.calculate_subtotal() + self.calculate_tax()

    def get_items(self):
        """Return copy of items list."""
        return self._items.copy()

    def __str__(self):
        """User-friendly string representation."""
        lines = [f"Invoice {self.invoice_id}"]
        lines.append("-" * 50)

        for item in self._items:
            product = item["product"]
            quantity = item["quantity"]
            line_total = product.price * quantity
            lines.append(f"  {product.name} x{quantity}: ${line_total:.2f}")

        lines.append("-" * 50)
        lines.append(f"Subtotal: ${self.calculate_subtotal():.2f}")
        lines.append(f"Tax ({self.tax_rate*100}%): ${self.calculate_tax():.2f}")
        lines.append(f"Total: ${self.calculate_total():.2f}")

        return "\n".join(lines)

    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Invoice(invoice_id={self.invoice_id!r}, items={len(self._items)}, total=${self.calculate_total():.2f})"
```

### 5. InvoiceManager

```python
import json

class InvoiceManager:
    """Manages collection of invoices."""

    def __init__(self):
        """Initialize invoice manager."""
        self.invoices = []

    def create_invoice(self, invoice_id, tax_rate=0.08):
        """
        Create new invoice.

        Args:
            invoice_id (str): Unique invoice ID
            tax_rate (float): Tax rate

        Returns:
            Invoice: New invoice instance
        """
        invoice = Invoice(invoice_id, tax_rate)
        self.invoices.append(invoice)
        return invoice

    def get_invoice(self, invoice_id):
        """
        Get invoice by ID.

        Args:
            invoice_id (str): Invoice ID to find

        Returns:
            Invoice or None: Invoice if found, None otherwise
        """
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                return invoice
        return None

    def list_invoices(self):
        """Return list of all invoices."""
        return self.invoices.copy()

    def save_to_file(self, filename):
        """
        Save all invoices to JSON file.

        Args:
            filename (str): Path to save file
        """
        try:
            data = []
            for invoice in self.invoices:
                invoice_data = {
                    "invoice_id": invoice.invoice_id,
                    "tax_rate": invoice.tax_rate,
                    "items": [
                        {
                            "product": item["product"].get_info(),
                            "quantity": item["quantity"]
                        }
                        for item in invoice.get_items()
                    ]
                }
                data.append(invoice_data)

            with open(filename, "w") as f:
                json.dump(data, f, indent=2)

            print(f"✓ Invoices saved to {filename}")

        except IOError as e:
            print(f"✗ Error saving invoices: {e}")

    def load_from_file(self, filename):
        """
        Load invoices from JSON file.

        Args:
            filename (str): Path to load file
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            # Clear existing invoices
            self.invoices = []

            # Reconstruct invoices (simplified - actual implementation needs product registry)
            print(f"✓ Loaded {len(data)} invoices from {filename}")
            print("⚠ Note: Product reconstruction requires product registry (implement as stretch goal)")

        except FileNotFoundError:
            print(f"✗ File not found: {filename}")
        except json.JSONDecodeError:
            print(f"✗ Invalid JSON format in {filename}")
        except IOError as e:
            print(f"✗ Error loading invoices: {e}")

    def __str__(self):
        """User-friendly string representation."""
        return f"InvoiceManager: {len(self.invoices)} invoices"
```

---

## User Flow

### 1. Main Menu

```
========================================
    Inventory & Invoice Manager
========================================

1. Product Management
2. Invoice Management
3. Save/Load Data
4. Exit

Choose an option:
```

### 2. Product Management Submenu

```
--- Product Management ---
1. Add Product
2. Update Product
3. Remove Product
4. Display All Products
5. Search Product
6. Back to Main Menu

Choose an option:
```

### 3. Invoice Management Submenu

```
--- Invoice Management ---
1. Create Invoice
2. Add Item to Invoice
3. Display Invoice
4. List All Invoices
5. Back to Main Menu

Choose an option:
```

### 4. Sample Interaction

```
Choose an option: 1

--- Product Management ---
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

## Implementation Guide

### Step 1: Create Product Classes (2-3 hours)

1. Implement `Product` base class with validation
2. Implement `PerishableProduct` with expiry logic
3. Implement `NonPerishableProduct` with warranty
4. Test each class individually

### Step 2: Create Invoice Class (1-2 hours)

1. Implement `Invoice` class
2. Test adding/removing items
3. Test calculations (subtotal, tax, total)

### Step 3: Create InvoiceManager (1-2 hours)

1. Implement `InvoiceManager` class
2. Test creating/retrieving invoices
3. Implement basic save/load (you can simplify this)

### Step 4: Build Console Interface (2-3 hours)

1. Create main menu loop
2. Implement product management submenu
3. Implement invoice management submenu
4. Connect all pieces together

### Step 5: Add Error Handling (1-2 hours)

1. Wrap user inputs in try/except
2. Handle file I/O errors
3. Validate all inputs
4. Add helpful error messages

### Step 6: Test Thoroughly (1-2 hours)

1. Test all features work
2. Test edge cases (empty inputs, negative values, missing files)
3. Test invalid data types
4. Test file save/load

---

## Testing Checklist

### Product Management
- [ ] Add perishable product with valid data
- [ ] Add non-perishable product with valid data
- [ ] Reject invalid product data (empty name, negative price/quantity)
- [ ] Update product price and quantity
- [ ] Remove product
- [ ] Display all products (formatted correctly)
- [ ] Search product by name/ID

### Invoice Management
- [ ] Create new invoice
- [ ] Add items to invoice
- [ ] Remove items from invoice
- [ ] Calculate subtotal correctly
- [ ] Calculate tax correctly
- [ ] Calculate total correctly (subtotal + tax)
- [ ] Display invoice details (formatted, readable)
- [ ] List all invoices

### File I/O
- [ ] Save products to JSON file
- [ ] Load products from JSON file
- [ ] Handle missing file (FileNotFoundError)
- [ ] Handle corrupted JSON (json.JSONDecodeError)
- [ ] Save invoices to JSON file
- [ ] Load invoices from JSON file

### Edge Cases
- [ ] Empty product name
- [ ] Negative price
- [ ] Negative quantity
- [ ] Invalid expiry date format
- [ ] Expired product warning
- [ ] Add more items than in stock
- [ ] Empty invoice
- [ ] Division by zero (shouldn't happen, but check)

---

## Stretch Goals (Optional)

- **Product Registry:** Centralized registry to track all products
- **Invoice-Product Linking:** Properly reconstruct invoices from files
- **Discount System:** Apply discounts to invoices
- **Product Categories:** Group products by category
- **Search Filters:** Search by price range, expiry date, etc.
- **Low Stock Alerts:** Warn when products are low in stock
- **Expired Product Reports:** List all expired products
- **Sales Analytics:** Total revenue, most sold products, etc.
- **Unit Tests:** Write proper unit tests with `unittest` or `pytest`
- **GUI:** Build a simple GUI with `tkinter`

---

## Submission Requirements

1. **Code files:**
   - `ims.py` (main program)
   - Or separate files: `product.py`, `invoice.py`, `main.py`

2. **README.md:**
   - How to run the program
   - Features implemented
   - Known limitations
   - Stretch goals attempted (if any)

3. **Sample data files:**
   - `products.json` (sample products)
   - `invoices.json` (sample invoices)

4. **Reflection log:**
   - [`../../reflection_log.md`](../../reflection_log.md) completed

---

## Grading

See [`../../final_project_rubric.md`](../../final_project_rubric.md) for detailed grading criteria.

**Summary:**
- **Functionality (40%):** All features work correctly
- **OOP Design (30%):** Proper use of classes, inheritance, polymorphism
- **Integration (20%):** Combines concepts from all 4 weeks
- **Code Quality (10%):** Readable, documented, tested

---

## Common Mistakes

See [`../../common_mistakes.md`](../../common_mistakes.md) for OOP-specific bugs to avoid.

**Top 3 mistakes to watch for:**
1. Forgetting `super().__init__()` in subclasses
2. Not handling file I/O exceptions
3. Not validating user inputs

---

## Need Help?

- **Re-read handbooks:** Week 4 sessions cover all concepts
- **Do Project 5 first:** If OOP feels shaky, RPG Arena is simpler
- **Run demo code:** Modify session demos to understand concepts
- **Office hours:** Check syllabus for schedule
- **Ask classmates:** Discuss concepts, not code

---

## Final Reminders

⚠️ **This is your final assessment:**
- Start Saturday (not Sunday night)
- Test thoroughly before submitting
- Handle edge cases
- Document your code
- Ask for help if stuck (don't suffer in silence)

**You've got this!** You've learned everything you need across 4 weeks. This project proves you can put it all together.

Good luck!
