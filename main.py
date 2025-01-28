from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Would you like some coffee?")
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Please select a drink ({options}) or type 'report' to see the resources and profit: ").lower()

    if choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
        break

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    if choice not in options:
        print("Sorry, that drink is not available. Please select another one.")
        continue

    drink = menu.find_drink(choice)

    print(f"The price for {drink.name} is {drink.cost} {money_machine.CURRENCY}")

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

