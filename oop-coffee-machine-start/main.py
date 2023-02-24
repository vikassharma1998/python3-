from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
obj = CoffeeMaker()
obj1 = MoneyMachine()
obj2 = Menu()
on_it = True
while on_it:
    options = obj2.get_items()
    choice = input(f" What Would you like {options}: ").lower()
    if choice == 'off':
        on_it = False
    elif choice == 'report':
        obj.report()
        obj1.report()
    else:
        drink = obj2.find_drink(choice)
        if obj.is_resource_sufficient(drink):
            if obj1.make_payment(drink.cost):
                obj.make_coffee(drink)
