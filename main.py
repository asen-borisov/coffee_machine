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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def calc_coins():
    """ Returns total inserted """
    print("Please insert coins.")
    total = 0
    total += 0.25 * int(input("how many quarters?: "))
    total += 0.10 * int(input("how many dimes?: "))
    total += 0.05 * int(input("how many nickles?: "))
    total += 0.01 * int(input("how many pennies?: "))
    return total


def have_resource(ingredients):
    """"Return True if enough resources  """
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print("Sorry there is not enough {item} ")
            return False
    return True


def transaction(money_received, drink_cost):
    """Return true if money is enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Please take your change ${change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct ingredients from resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your drink {drink} ☕")


is_on = True

while is_on:
    user_input = (input("What would you like? (espresso/latte/cappuccino): "))
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f''' 
                water = {water}ml.
                coffee = {coffee}gr. 
                milk = {milk}ml.
                money = ${money}
            ''')
    else:
        drink = MENU[user_input]
        if have_resource(drink["ingredients"]):
            payment = calc_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
