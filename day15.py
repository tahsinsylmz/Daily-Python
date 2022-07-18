# Coffee machine project
menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def enter_money():
    a = 0
    a += int(input("how many quarters: ")) * 0.25
    a += int(input("how many dimes: ")) * 0.1
    a += int(input("how many nickles: ")) * 0.05
    a += int(input("how many pennies: ")) * 0.01
    return a


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def have_enough():
    if choice == "espresso":
        if resources["water"] >= menu["espresso"]["ingredients"]["water"] and resources["coffee"] >= menu["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif choice == "latte":
        if resources["water"] >= menu["latte"]["ingredients"]["water"] and resources["milk"] >= menu["latte"]["ingredients"]["milk"] and resources["coffee"] >= menu["latte"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif choice == "cappuccino":
        if resources["water"] >= menu["cappuccino"]["ingredients"]["water"] and resources["milk"] >= menu["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= menu["cappuccino"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    else:
        print("The value you entered was not found, please re-type")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


choice = ""
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if have_enough():
            payment = enter_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])
        else:
            is_resource_sufficient(menu[choice]["ingredients"])



