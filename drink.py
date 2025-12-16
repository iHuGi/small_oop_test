from abc import ABC, abstractmethod


# --- 1. ABSTRACTION (The Blueprint) ---
# 'Drink' is an Abstract Base Class (ABC).
# It sets the mandatory structure for all concrete drink types.
class Drink(ABC):
    """Abstract Base Class for all menu items."""
    def __init__(self, name: str, price: float):
        # ABSTRACTION: All drinks share these core properties.
        self.name = name
        self.price = price

    @abstractmethod
    def make(self) -> str:
        # ABSTRACTION: This method MUST be implemented by every child class.
        # It defines the contract: every drink must know how to be made.
        """Every drink must implement how it is made."""
        pass

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


# --- 2. INHERITANCE & POLYMORPHISM (Specific Items) ---

# INHERITANCE: Coffee is-a Drink, so it automatically gets 'name' and 'price'.
class Coffee(Drink):
    def __init__(self, name: str, price: float, roast_level: str):
        # INHERITANCE: Calls the parent (Drink) class's constructor.
        super().__init__(name, price)
        self.roast_level = roast_level

    def make(self) -> str:
        # POLYMORPHISM: This is Coffee's unique implementation of the abstract 'make' method.
        """Coffee making process."""
        return f"☕ Grinding {self.roast_level} beans... Brewing {self.name}!"


# INHERITANCE: Tea is-a Drink.
class Tea(Drink):
    def __init__(self, name: str, price: float, tea_type: str):
        # INHERITANCE: Calls the parent (Drink) class's constructor.
        super().__init__(name, price)
        self.tea_type = tea_type

    def make(self) -> str:
        # POLYMORPHISM: This is Tea's unique implementation of the abstract 'make' method.
        # Note how the method signature is the same as Coffee.make(), but the logic is different.
        """Tea making process."""
        return f"🍵 Steeping {self.tea_type} leaves for 3 minutes... Pouring {self.name}!"


# INHERITANCE: Soda is-a Drink.
class Soda(Drink):
    def __init__(self, name: str, price: float, sugar_amount: float):
        # INHERITANCE: Calls the parent (Drink) class's constructor.
        super().__init__(name, price)
        self.sugar_amount = sugar_amount # Sugar amount in grams

    def make(self) -> str:
        # POLYMORPHISM: This is Soda's unique implementation of the abstract 'make' method.
        """Soda serving process."""
        return f"🥤 Dispensing {self.name}. Sugar amount: {self.sugar_amount:.2f}g."