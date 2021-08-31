
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def machine(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    elif MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    else:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_pay = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        if total_pay < MENU[coffee_type]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["money"] += total_pay
            change = total_pay - MENU[coffee_type]["cost"]
            print(f"Here is ${change} dollars in change")
            resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
            print(f"Here is your {userInput}. Enjoy!")


while True:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")

    if userInput == "off":
        print("good bye")
        break
    elif userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif userInput == "espresso":
        machine("espresso")
    elif userInput == "latte":
        machine("latte")
    elif userInput == "cappuccino":
        machine("cappuccino")
