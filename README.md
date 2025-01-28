# Coffee Machine

A simple coffee machine simulation project built with Python. The program allows users to order coffee drinks, manage resources (water, milk, coffee), and process payments. The goal is to practice object-oriented programming in Python.

## Features

- Users can choose from three coffee drinks: Latte, Espresso, and Cappuccino.
- The program checks if there are enough resources (water, milk, coffee) to make the drink.
- Users are prompted to insert coins (quarters, dimes, nickels, pennies) to pay for the drink.
- If payment is successful, the drink is prepared and resources are deducted.
- Users can view a report of the current resources and total profit.
- Users can turn off the coffee machine.

## Menu

The available drinks are:

1. **Latte**: Costs $2.5, requires 200ml of water, 150ml of milk, and 24g of coffee.
2. **Espresso**: Costs $1.5, requires 50ml of water, no milk, and 18g of coffee.
3. **Cappuccino**: Costs $3, requires 250ml of water, 50ml of milk, and 24g of coffee.

## Requirements

Make sure to have Python 3.x installed. This project doesn't require any external libraries, as it is designed to be a simple command-line interface (CLI) application.

## How to Use

1. Run the main Python file:
    ```bash
    python main.py
    ```

2. Choose from the following options:
    - Type the name of the coffee you want to order (e.g., "latte", "espresso", "cappuccino").
    - Type "report" to check the current resources and profit.
    - Type "off" to exit the program.

3. The program will:
    - Show the price of the selected drink.
    - Deduct resources if there are enough.
    - Request payment from the user.
    - Make the coffee if payment is successful.

## Code Structure

The code consists of four main components:

- **CoffeeMaker**: Manages the resources and makes coffee.
- **Menu**: Contains the available drink items and prices.
- **MoneyMachine**: Handles the payment process and tracks the profit.
- **Main File (main.py)**: The entry point that ties everything together.

## Example Interaction

Welcome to the Coffee Machine! Please select a drink (latte/espresso/cappuccino) or type 'report' to see the resources and profit: latte The price for latte is $2.5 Please insert coins. How many quarters?: 2 How many dimes?: 1 How many nickles?: 0 How many pennies?: 4 Here is $1.25 in change. Here is your latte ☕️. Enjoy!


## License

This project is open-source and available under the [MIT License](LICENSE).
