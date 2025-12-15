# ☕ Coffee Shop Order System (OOP Refresher)

A small Python program designed to refresh core Object-Oriented Programming (OOP) principles through an in-memory simulation of a coffee shop order system.

## ✨ Key Concepts Demonstrated

This project showcases the four pillars of OOP:

| Concept | Demonstrated By | Explanation |
| :--- | :--- | :--- |
| **Abstraction** | `Drink` Abstract Base Class (ABC) | Defines the contract (what every item on the menu **must** have: `name`, `price`, and a `make()` method). |
| **Inheritance** | `Coffee(Drink)` and `Tea(Drink)` | Specialized classes inherit common properties (`name`, `price`) from the generic `Drink` parent class. |
| **Polymorphism** | `make()` method in both children | The same method call (`drink.make()`) executes different, type-specific logic (e.g., grinding/brewing vs. steeping). |
| **Encapsulation** | `Register` class and `__balance` | The cash register's balance is kept private (`__balance`) and can only be modified through the controlled public method (`add_order`). |

## 🚀 Getting Started

### Prerequisites

You need a working installation of Python (3.6+ is recommended).

### How to Run

Execute the main program file directly:

```bash
python main.py
```

### Expected Output

The program will run through the process of taking orders, processing them, and displaying the final total revenue.

> **Note:** This program uses an in-memory system. All order data and the final balance are lost when the program ends.

## 📁 Project Structure

```
coffee-shop-oop/
├── main.py             # The core Python program with all classes and execution logic
├── .gitignore          # Specifies files to ignore (e.g., venvs, IDE settings)
└── README.md           # This file
```