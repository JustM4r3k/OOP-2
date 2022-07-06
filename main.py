from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()


while True:
    print(menu.get_items())
    choice = input("what would you like?: ")

    if choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif choice == "off":
        break
    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if coffeemaker.is_resource_sufficient(drink):
                if moneymachine.make_payment(drink.cost):
                    coffeemaker.make_coffee(drink)