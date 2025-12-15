from abc import ABC, abstractmethod


# --- 1. ABSTRACTION (The Blueprint) ---
class Drink(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def make(self):
        """Every drink must implement how it is made."""
        pass

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"


# --- 2. INHERITANCE & POLYMORPHISM (Specific Items) ---
class Coffee(Drink):
    def __init__(self, name, price, roast_level):
        super().__init__(name, price)
        self.roast_level = roast_level

    def make(self):
        # Polymorphism: Coffee is made differently than Tea
        return f"☕ Grinding {self.roast_level} beans... Brewing {self.name}!"


class Tea(Drink):
    def __init__(self, name, price, tea_type):
        super().__init__(name, price)
        self.tea_type = tea_type

    def make(self):
        # Polymorphism: Tea logic is unique
        return f"🍵 Steeping {self.tea_type} leaves for 3 minutes... Pouring {self.name}!"


# --- 3. ENCAPSULATION (The Cash Register) ---
class Register:
    def __init__(self):
        self.__balance = 0.0  # Private attribute (note the double underscore)
        self.orders = []

    def add_order(self, drink):
        if isinstance(drink, Drink):
            self.orders.append(drink)
            self.__update_balance(drink.price)  # Internal method call
            print(f"Order added: {drink}")
        else:
            print("Invalid item!")

    def __update_balance(self, amount):
        # Private method: Only the register itself can change the money
        self.__balance += amount

    def get_total_sales(self):
        # Getter: Controlled access to private data
        return self.__balance

    def process_all_orders(self):
        print("\n--- 🚀 Processing Orders ---")
        if not self.orders:
            print("No orders to process.")

        for drink in self.orders:
            print(drink.make())

        # Clear orders after processing
        self.orders.clear()


# --- 4. EXECUTION (The Main Loop) ---
if __name__ == "__main__":
    # Create the shop's register
    my_shop_register = Register()

    # Create distinct objects
    dark_roast = Coffee("Espresso", 3.50, "Dark Roast")
    green_tea = Tea("Green Tea", 2.75, "Jasmine")
    latte = Coffee("Vanilla Latte", 4.50, "Medium Roast")

    # The interaction
    my_shop_register.add_order(dark_roast)
    my_shop_register.add_order(green_tea)
    my_shop_register.add_order(latte)

    # Encapsulation check: Trying to hack the register
    # my_shop_register.__balance = 1000000  # <--- This would throw an error or be ignored in strict contexts

    # Process the queue
    my_shop_register.process_all_orders()

    # Check totals
    print(f"\n💰 Total Daily Revenue: ${my_shop_register.get_total_sales():.2f}")