from resources import resources
from resources import MENU
from prettytable import PrettyTable


def check_resources(order):
    water_req = MENU[order]['ingredients']['water']
    coffee_req = MENU[order]['ingredients']['coffee']

    if order == 'espresso':
        milk_req = 0
    else:
        milk_req = MENU[order]['ingredients']['milk']

    if available_resources['water'] < water_req:
        print("Sorry, There is not enough water")
        return 'false'
    elif available_resources['coffee'] < coffee_req:
        print("Sorry, There is not enough coffee")
        return 'false'
    elif available_resources['milk'] < milk_req:
        print("Sorry, There is not enough milk")
        return 'false'
    else:
        return 'true'


def deduct_resources(order):
    water_req = MENU[order]['ingredients']['water']
    coffee_req = MENU[order]['ingredients']['coffee']

    if order == 'espresso':
        milk_req = 0
    else:
        milk_req = MENU[order]['ingredients']['milk']
    available_resources['water'] -= water_req
    available_resources['coffee'] -= coffee_req
    available_resources['milk'] -= milk_req


def process_coins(cost):
    print("Please insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    payment = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if payment < cost:
        print("Sorry that's not enough money. Money refunded")
        return 'false'
    else:
        payment -= cost
        print(f"Here is your ${round(payment,2)} in change.")
        return 'true'


def check_order(order):
    if order == 'report':
        print(available_resources)
    elif order == 'espresso' or 'latte' or 'cappuccino':
        if check_resources(order) == 'true':
            if process_coins(MENU[order]['cost']) == 'true':
                deduct_resources(order)
                available_resources['money'] += MENU[order]['cost']
                print(f"Here is your {order}.Enjoy!")
    else:
        print('invalid order')


order = input("What would you like? (espresso/latte/cappuccino):").lower()
available_resources = resources
available_resources['money'] = 0
table = PrettyTable()
print(table)


while order != 'off':
    check_order(order)
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
