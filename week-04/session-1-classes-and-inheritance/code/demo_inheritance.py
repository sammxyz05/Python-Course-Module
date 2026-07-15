"""
Demo: Inheritance Basics
Shows: base class, subclass, super(), method overriding, extending methods
"""

# Base class (parent, superclass)
class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        """Describe the vehicle."""
        return f"{self.year} {self.brand} {self.model}"

    def start(self):
        """Start the vehicle."""
        return f"The {self.brand} {self.model} is starting..."


# Derived class (child, subclass)
class Car(Vehicle):
    """Car inherits from Vehicle."""

    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)  # Call parent's __init__
        self.num_doors = num_doors

    def describe(self):
        """Override parent's describe method."""
        base_description = super().describe()  # Get parent's description
        return f"{base_description} with {self.num_doors} doors"

    def honk(self):
        """Car-specific method."""
        return "Beep beep!"


class Motorcycle(Vehicle):
    """Motorcycle inherits from Vehicle."""

    def __init__(self, brand, model, year, has_sidecar=False):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        """Motorcycle-specific method."""
        return "Doing a wheelie!"


# Usage
print("=== Creating vehicles ===")
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, has_sidecar=False)

# Inherited methods
print(car.describe())        # Uses overridden method
print(car.start())           # Inherited from Vehicle
print(motorcycle.describe()) # Inherited from Vehicle
print(motorcycle.start())    # Inherited from Vehicle

# Subclass-specific methods
print(car.honk())            # Car-specific
print(motorcycle.wheelie())  # Motorcycle-specific

# Inherited attributes
print(f"\nCar year: {car.year}")
print(f"Motorcycle brand: {motorcycle.brand}")

# Subclass-specific attributes
print(f"Car doors: {car.num_doors}")
print(f"Motorcycle sidecar: {motorcycle.has_sidecar}")


# Checking types and inheritance
print("\n=== Type checking ===")
print(f"car is a Car: {isinstance(car, Car)}")
print(f"car is a Vehicle: {isinstance(car, Vehicle)}")
print(f"motorcycle is a Motorcycle: {isinstance(motorcycle, Motorcycle)}")
print(f"motorcycle is a Vehicle: {isinstance(motorcycle, Vehicle)}")
print(f"Car is subclass of Vehicle: {issubclass(Car, Vehicle)}")


# Multiple levels of inheritance
print("\n=== Multiple levels ===")

class ElectricCar(Car):
    """ElectricCar inherits from Car, which inherits from Vehicle."""

    def __init__(self, brand, model, year, num_doors, battery_capacity):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def describe(self):
        """Override Car's describe method."""
        base_description = super().describe()
        return f"{base_description}, {self.battery_capacity}kWh battery"

    def charge(self):
        """ElectricCar-specific method."""
        return "Charging battery..."


tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)
print(tesla.describe())  # Uses all three classes' describe methods
print(tesla.start())     # Inherited from Vehicle
print(tesla.honk())      # Inherited from Car
print(tesla.charge())    # ElectricCar-specific

print(f"tesla is a ElectricCar: {isinstance(tesla, ElectricCar)}")
print(f"tesla is a Car: {isinstance(tesla, Car)}")
print(f"tesla is a Vehicle: {isinstance(tesla, Vehicle)}")
