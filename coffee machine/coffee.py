MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
coffee_shop_on = True
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(ingredients):
    for items in ingredients:
        if ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

def check_payment():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2 )
        print(f"Here is ${change} in change.")
        profit +=drink_cost
        return True
    else:
        return False
def make_coffee(drink_name,ingreadient):
    for item in ingreadient:
       resources[item] -= ingreadient[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
on_it = True
while on_it:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        on_it = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee{resources['coffee']}g \nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            paymeny = check_payment()
            if is_transaction_successful(paymeny, drink['cost']):
                make_coffee(choice, drink['ingredients'])
