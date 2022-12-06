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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def resource(order_ingredients):
    """
    :param order_ingredients:
    :return: True when order can be made and False when ingredients are insufficient.
    """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item}")
            is_enough = False
            return False
    return is_enough


def process_coins():

    """
    :returns total from the coins inserted
    """
    print("Please insert coins: ")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many dimes? :")) * 0.1
    total += int(input("How many nickels? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):

    """
    :param money_received:
    :param drink_cost:
    :return: True if  payment accepted, False if money is insufficient.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money, Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    deduct the required ingredients from the resources.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f" Here is your {drink_name} ☕ Enjoy!")


isOn = True

while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"water: {resources['water']}g")
        print(f"milk: {resources['milk']}g")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])







