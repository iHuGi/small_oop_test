# MODULARIZATION: This file imports classes defined in other modules (.py files).
# This is how the different pieces of the program are connected..
from register import Register
from drink import Coffee, Tea, Soda # Import all necessary classes

if __name__ == "__main__":
    # --- Setup ---
    # INTEGRATION: Instantiate the Register object, making the cash system available.
    my_shop_register = Register()

    # --- Create Distinct Objects ---
    # INHERITANCE: Creating specialized objects (Coffee, Tea, Soda) that all share the 'Drink' type.
    dark_roast = Coffee("Espresso", 3.50, "Dark Roast")
    green_tea = Tea("Green Tea", 2.75, "Jasmine")
    vanilla_latte = Coffee("Vanilla Latte", 4.50, "Medium Roast")
    diet_cola = Soda("Diet Cola", 1.99, 0.0)
    classic_soda = Soda("Classic Orange", 2.25, 45.5)

    print("\n--- 🛒 Taking Orders ---")

    # --- The Interaction ---
    # ENCAPSULATION/INTERACTION: Calls the public method of the Register to add an order.
    # The Register handles the internal state change (updating __balance).
    my_shop_register.add_order(dark_roast)
    my_shop_register.add_order(green_tea)
    my_shop_register.add_order(vanilla_latte)
    my_shop_register.add_order(diet_cola)
    my_shop_register.add_order(classic_soda)

    # --- Process Queue ---
    # POLYMORPHISM: When Register calls 'drink.make()', Python executes the correct 'make()'
    # method based on the object's type (Coffee's make, Tea's make, etc.).
    my_shop_register.process_all_orders()

    # --- Check Totals ---
    # ENCAPSULATION: Accesses the protected data (__balance) using the public getter method.
    print(f"\n💰 Total Daily Revenue: ${my_shop_register.get_total_sales():.2f}")