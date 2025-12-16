#☕ Coffee Shop Order System (OOP Refresher)A Python program designed to refresh core Object-Oriented Programming (OOP) principles through an in-memory simulation of a coffee shop order system, utilizing a **modular architecture**.

##✨ Key Concepts DemonstratedThis project showcases the four pillars of OOP:

| Concept | Demonstrated By | Explanation |
| --- | --- | --- |
| **Abstraction** | `Drink` Abstract Base Class (ABC) | Defines the contract (what every menu item **must** implement: `name`, `price`, and a `make()` method). |
| **Inheritance** | `Coffee(Drink)`, `Tea(Drink)`, `Soda(Drink)` | Specialized classes inherit common properties from the generic `Drink` parent class. |
| **Polymorphism** | The `make()` method | The same method call (`drink.make()`) executes different, type-specific logic for Coffee, Tea, and Soda. |
| **Encapsulation** | `Register` class and `__balance` | The cash register's balance is kept private (`__balance`) and can only be modified through controlled public methods (`add_order`, `get_total_sales`). |

##🚀 Getting Started###PrerequisitesYou need a working installation of Python (3.6+ is recommended).

###How to RunExecute the main **entry-point** file (**`main_v2.py`**) directly from the project root:

```bash
python main_v2.py

```

###Expected OutputThe program will run through the process of creating various drinks, adding them to the register, processing all orders using polymorphism, and displaying the final total revenue.

> **Note:** This program uses an in-memory system. All order data and the final balance are lost when the program ends.

##📁 Updated Project StructureThis structure adheres to best practices by separating concerns into dedicated modules.

```
coffee-shop-oop/
├── main_v2.py          # The main execution file (The Controller/Client Code).
├── drink.py            # Contains the Abstraction (Drink) and Inheritance (Coffee, Tea, Soda) classes.
├── register.py         # Contains the Encapsulation logic (Register class).
├── .venv/              # (Optional) Your Python Virtual Environment.
└── README.md           # This file

```