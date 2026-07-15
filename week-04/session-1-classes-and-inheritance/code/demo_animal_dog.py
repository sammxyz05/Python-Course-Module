"""
Demo: Animal and Dog (live-coded example)
Shows: Inheritance with private attributes, encapsulation, super()
This is the exact example from the master schedule and class lecture.
"""

class Animal:
    """Base class representing any animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.__sound = "generic animal sound"  # Private attribute

    def make_sound(self):
        """Make the animal's sound."""
        print(f"{self.name} says: {self.__sound}")

    def describe(self):
        """Describe the animal."""
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name, breed):
        # Call parent's __init__ with species="dog"
        super().__init__(name, species="dog")
        self.breed = breed
        # Note: We don't override __sound here because it's private in parent

    def describe(self):
        """Override to include breed."""
        base_description = super().describe()
        return f"{base_description} (breed: {self.breed})"

    def bark(self):
        """Dog-specific behavior."""
        print(f"{self.name} barks: Woof! Woof!")

    def fetch(self, item):
        """Dog-specific behavior."""
        print(f"{self.name} fetches the {item}!")


# Create instances
print("=== Creating animals ===")
generic_animal = Animal("Unknown", "mystery creature")
buddy = Dog("Buddy", "Golden Retriever")
max_dog = Dog("Max", "German Shepherd")

# Using inherited methods
print("\n=== Describing animals ===")
print(generic_animal.describe())
print(buddy.describe())
print(max_dog.describe())

# Using inherited make_sound method
print("\n=== Making sounds ===")
generic_animal.make_sound()  # Uses parent's private __sound
buddy.make_sound()           # Also uses parent's private __sound

# Dog-specific methods
print("\n=== Dog-specific behaviors ===")
buddy.bark()
buddy.fetch("ball")

max_dog.bark()
max_dog.fetch("frisbee")

# Demonstrating that __sound is private
print("\n=== Private attribute demonstration ===")
try:
    print(buddy.__sound)  # This will fail
except AttributeError as e:
    print(f"Error accessing __sound directly: {e}")

# But it's still accessible via name mangling (don't do this in real code!)
print(f"Accessing via name mangling: {buddy._Animal__sound}")

# Checking inheritance
print("\n=== Type checking ===")
print(f"buddy is a Dog: {isinstance(buddy, Dog)}")
print(f"buddy is an Animal: {isinstance(buddy, Animal)}")
print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")


# More advanced example: extending the hierarchy
print("\n=== Extending the hierarchy ===")

class ServiceDog(Dog):
    """Service dog is a specialized type of dog."""

    def __init__(self, name, breed, service_type):
        super().__init__(name, breed)
        self.service_type = service_type

    def describe(self):
        """Override to include service type."""
        base_description = super().describe()
        return f"{base_description}, trained as {self.service_type}"

    def assist(self):
        """Service-specific behavior."""
        print(f"{self.name} is assisting as a {self.service_type} dog")


guide_dog = ServiceDog("Luna", "Labrador", "guide dog")
print(guide_dog.describe())
guide_dog.make_sound()  # Inherited from Animal
guide_dog.bark()        # Inherited from Dog
guide_dog.fetch("harness")  # Inherited from Dog
guide_dog.assist()      # ServiceDog-specific

print(f"\nluna is a ServiceDog: {isinstance(guide_dog, ServiceDog)}")
print(f"luna is a Dog: {isinstance(guide_dog, Dog)}")
print(f"luna is an Animal: {isinstance(guide_dog, Animal)}")
