# We need to import the Drink base class to check the type in add_order
from drink import Drink


# --- 3. ENCAPSULATION (The Cash Register) ---
class Register:
    """Manages orders, transactions, and total sales, keeping internal state secure."""

    def __init__(self):
        # ENCAPSULATION: This is a private attribute (indicated by __).
        # It represents the internal state (money) that should only be changed by the Register itself.
        self.__balance = 0.0
        self.orders = []

    def add_order(self, drink):
        """Adds a valid drink to the orders and updates the private balance."""
        # ENCAPSULATION: We use type checking (isinstance) to ensure only valid objects
        # that follow the Drink contract can enter the system.
        if isinstance(drink, Drink):
            self.orders.append(drink)

            # ENCAPSULATION: The public method 'add_order' delegates the sensitive change
            # to the internal (private) method '__update_balance'.
            self.__update_balance(drink.price)
            print(f"Order added: {drink}")
        else:
            print("Invalid item!")

    def __update_balance(self, amount):
        # ENCAPSULATION: This is a private method.
        # It ensures that money is only added or subtracted through controlled logic
        # inside the Register class, preventing external accidental or malicious changes.
        self.__balance += amount

    def get_total_sales(self):
        # ENCAPSULATION: This is a "Getter" method.
        # It provides read-only access to the private attribute (__balance),
        # maintaining control over how the internal state is viewed.
        return self.__balance

    def process_all_orders(self):
        """Processes all orders using polymorphism (drink.make())."""
        print("\n--- 🚀 Processing Orders ---")
        if not self.orders:
            print("No orders to process.")

        # POLYMORPHISM: The loop doesn't care if it's Coffee, Tea, or Soda.
        # It just calls 'make()', and the right code runs based on the object's type.
        for drink in self.orders:
            print(drink.make())

        # Clear orders after processing
        self.orders.clear()