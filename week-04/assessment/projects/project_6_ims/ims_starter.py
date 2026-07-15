"""
Project 6: Inventory & Invoice Management System (IMS)
MANDATORY FINAL PROJECT - Due Wednesday night

This is a starter template. Follow PROJECT_SPEC.md for detailed requirements.
"""

from datetime import datetime
import json


# ============================================================================
# PRODUCT CLASSES
# ============================================================================

# TODO 1: Implement Product base class
# Requirements:
# - __init__(name, product_id, price, quantity) with validation
# - Validate: name is non-empty string, price >= 0, quantity >= 0
# - Methods: update_price(new_price), update_quantity(new_quantity)
# - Method: get_info() returns dict with product info
# - Magic methods: __str__, __repr__

class Product:
    """Base class for all products."""
    pass  # Replace with your code


# TODO 2: Implement PerishableProduct subclass
# Requirements:
# - Inherit from Product
# - __init__(name, product_id, price, quantity, expiry_date)
# - Call super().__init__() for base attributes
# - Validate expiry_date format (YYYY-MM-DD)
# - Methods: is_expired(), days_until_expiry()
# - Override: get_info() to include expiry_date
# - Override: __str__ to show expiry status

class PerishableProduct(Product):
    """Perishable product with expiry date."""
    pass  # Replace with your code


# TODO 3: Implement NonPerishableProduct subclass
# Requirements:
# - Inherit from Product
# - __init__(name, product_id, price, quantity, warranty_years)
# - Call super().__init__() for base attributes
# - Validate warranty_years >= 0
# - Method: has_warranty() returns True if warranty_years > 0
# - Override: get_info() to include warranty_years
# - Override: __str__ to show warranty info

class NonPerishableProduct(Product):
    """Non-perishable product with warranty."""
    pass  # Replace with your code


# ============================================================================
# INVOICE CLASSES
# ============================================================================

# TODO 4: Implement Invoice class
# Requirements:
# - __init__(invoice_id, tax_rate=0.08)
# - Attribute: _items (private list of dicts with product and quantity)
# - Method: add_item(product, quantity) - validate quantity, check stock
# - Method: remove_item(product_id)
# - Method: calculate_subtotal() - sum of (price * quantity)
# - Method: calculate_tax() - subtotal * tax_rate
# - Method: calculate_total() - subtotal + tax
# - Method: get_items() - returns copy of items
# - Magic methods: __str__ (formatted invoice), __repr__

class Invoice:
    """Invoice containing multiple product items."""
    pass  # Replace with your code


# TODO 5: Implement InvoiceManager class
# Requirements:
# - __init__() - initializes empty list of invoices
# - Method: create_invoice(invoice_id, tax_rate) - creates and stores invoice
# - Method: get_invoice(invoice_id) - finds invoice by ID
# - Method: list_invoices() - returns copy of invoices list
# - Method: save_to_file(filename) - saves invoices to JSON
# - Method: load_from_file(filename) - loads invoices from JSON
# - Handle exceptions: FileNotFoundError, json.JSONDecodeError, IOError
# - Magic method: __str__

class InvoiceManager:
    """Manages collection of invoices."""
    pass  # Replace with your code


# ============================================================================
# USER INTERFACE
# ============================================================================

# Global data structures (you can modify this approach)
products = []  # List of Product instances
invoice_manager = InvoiceManager()


def display_main_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("    Inventory & Invoice Manager")
    print("=" * 40)
    print("1. Product Management")
    print("2. Invoice Management")
    print("3. Save/Load Data")
    print("4. Exit")


def display_product_menu():
    """Display product management submenu."""
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Remove Product")
    print("4. Display All Products")
    print("5. Search Product")
    print("6. Back to Main Menu")


def display_invoice_menu():
    """Display invoice management submenu."""
    print("\n--- Invoice Management ---")
    print("1. Create Invoice")
    print("2. Add Item to Invoice")
    print("3. Display Invoice")
    print("4. List All Invoices")
    print("5. Back to Main Menu")


# TODO 6: Implement add_product()
# Requirements:
# - Prompt user for product type (perishable/non-perishable)
# - Prompt for product details (name, ID, price, quantity, + type-specific)
# - Validate all inputs (use try/except)
# - Create appropriate Product instance
# - Add to products list
# - Handle ValueError for invalid inputs

def add_product():
    """Add new product to inventory."""
    pass  # Replace with your code


# TODO 7: Implement update_product()
# Requirements:
# - Prompt for product ID
# - Find product in products list
# - Prompt for what to update (price or quantity)
# - Update and display confirmation
# - Handle case when product not found

def update_product():
    """Update existing product."""
    pass  # Replace with your code


# TODO 8: Implement remove_product()
# Requirements:
# - Prompt for product ID
# - Find and remove product from products list
# - Display confirmation
# - Handle case when product not found

def remove_product():
    """Remove product from inventory."""
    pass  # Replace with your code


# TODO 9: Implement display_all_products()
# Requirements:
# - Check if products list is empty
# - Loop through products and print each (use __str__)
# - Format nicely with separators

def display_all_products():
    """Display all products in inventory."""
    pass  # Replace with your code


# TODO 10: Implement search_product()
# Requirements:
# - Prompt for search term (name or ID)
# - Search products list (case-insensitive for name)
# - Display matching products
# - Handle case when no matches found

def search_product():
    """Search for product by name or ID."""
    pass  # Replace with your code


# TODO 11: Implement create_invoice()
# Requirements:
# - Prompt for invoice ID
# - Prompt for tax rate (with default)
# - Use invoice_manager.create_invoice()
# - Display confirmation

def create_invoice():
    """Create new invoice."""
    pass  # Replace with your code


# TODO 12: Implement add_item_to_invoice()
# Requirements:
# - Prompt for invoice ID
# - Get invoice from invoice_manager
# - Display available products
# - Prompt for product ID and quantity
# - Find product in products list
# - Add item to invoice (handle exceptions)
# - Display confirmation

def add_item_to_invoice():
    """Add item to existing invoice."""
    pass  # Replace with your code


# TODO 13: Implement display_invoice()
# Requirements:
# - Prompt for invoice ID
# - Get invoice from invoice_manager
# - Display invoice (use __str__)
# - Handle case when invoice not found

def display_invoice():
    """Display invoice details."""
    pass  # Replace with your code


# TODO 14: Implement list_all_invoices()
# Requirements:
# - Get all invoices from invoice_manager
# - Display each invoice's summary (ID, item count, total)
# - Handle empty list

def list_all_invoices():
    """List all invoices."""
    pass  # Replace with your code


# TODO 15: Implement save_data()
# Requirements:
# - Prompt for filename or use default
# - Convert products list to JSON-serializable format
# - Save to file with error handling
# - Use invoice_manager.save_to_file() for invoices
# - Display confirmation

def save_data():
    """Save products and invoices to files."""
    pass  # Replace with your code


# TODO 16: Implement load_data()
# Requirements:
# - Prompt for filename or use default
# - Load products from JSON file
# - Reconstruct Product instances (check type)
# - Handle FileNotFoundError, json.JSONDecodeError
# - Use invoice_manager.load_from_file() for invoices
# - Display confirmation

def load_data():
    """Load products and invoices from files."""
    pass  # Replace with your code


# TODO 17: Implement main loop
# Requirements:
# - Display main menu
# - Get user choice
# - Route to appropriate submenu or function
# - Use try/except for invalid inputs
# - Loop until user chooses Exit

def main():
    """Main program loop."""
    print("Welcome to IMS!")

    while True:
        display_main_menu()
        choice = input("\nChoose an option: ").strip()

        # Your code here
        pass


if __name__ == "__main__":
    main()


# ============================================================================
# TESTING SECTION (uncomment to test individual components)
# ============================================================================

# Test 1: Create and validate Product
# try:
#     p1 = Product("Laptop", "P001", 999.99, 10)
#     print(p1)
#     print(repr(p1))
# except ValueError as e:
#     print(f"Error: {e}")

# Test 2: Test invalid Product (should raise ValueError)
# try:
#     p2 = Product("", "P002", 50, 5)  # Empty name
# except ValueError as e:
#     print(f"Caught error: {e}")

# try:
#     p3 = Product("Item", "P003", -10, 5)  # Negative price
# except ValueError as e:
#     print(f"Caught error: {e}")

# Test 3: Create PerishableProduct
# try:
#     pp1 = PerishableProduct("Milk", "PP001", 4.99, 50, "2026-07-20")
#     print(pp1)
#     print(f"Expired: {pp1.is_expired()}")
#     print(f"Days until expiry: {pp1.days_until_expiry()}")
#     print(pp1.get_info())
# except ValueError as e:
#     print(f"Error: {e}")

# Test 4: Create NonPerishableProduct
# np1 = NonPerishableProduct("Keyboard", "NP001", 79.99, 20, 2)
# print(np1)
# print(f"Has warranty: {np1.has_warranty()}")
# print(np1.get_info())

# Test 5: Create Invoice and add items
# invoice = Invoice("INV001", 0.08)
# product1 = Product("Mouse", "P001", 25.99, 10)
# product2 = Product("Monitor", "P002", 299.99, 5)
#
# try:
#     invoice.add_item(product1, 2)
#     invoice.add_item(product2, 1)
#     print(invoice)
# except ValueError as e:
#     print(f"Error: {e}")

# Test 6: Try to add more than available stock (should raise ValueError)
# try:
#     invoice.add_item(product2, 10)  # Only 5 in stock
# except ValueError as e:
#     print(f"Caught error: {e}")

# Test 7: Test InvoiceManager
# manager = InvoiceManager()
# inv1 = manager.create_invoice("INV001", 0.08)
# inv2 = manager.create_invoice("INV002", 0.10)
# print(manager)
#
# found = manager.get_invoice("INV001")
# print(f"Found: {found}")
#
# not_found = manager.get_invoice("INV999")
# print(f"Not found: {not_found}")

# Test 8: Test file save/load
# manager.save_to_file("test_invoices.json")
# manager2 = InvoiceManager()
# manager2.load_from_file("test_invoices.json")
