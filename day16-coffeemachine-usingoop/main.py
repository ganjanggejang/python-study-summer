from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def machine(coffee_type):
    cost = 0
    choice = menu.find_drink(coffee_type)  # choice 안에는 객체가 통째로 들어있음
    is_sufficient = coffee_maker.is_resource_sufficient(choice)  # 재료가 충분하면, is_sufficient에 True를 저장
    # 만약 재료가 충분히 있다면, 만들 커피의 가격을 cost에 저장
    if is_sufficient:
        for item in menu.menu:
            if item == choice:
                cost = item.cost
        # make_payment() 메서드를 작동시켜 동전을 받고, 커피 가격 이상으로 돈을 받았다면 True를 is_payment_sufficient에 저장
        is_payment_sufficient = money_machine.make_payment(cost)
        if is_payment_sufficient:
            coffee_maker.make_coffee(choice)


while True:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")

    if userInput == "off":
        print("good bye")
        break
    elif userInput == "report":
        coffee_maker.report()
        money_machine.report()
    elif userInput == "espresso":
        machine("espresso")
    elif userInput == "latte":
        machine("latte")
    elif userInput == "cappuccino":
        machine("cappuccino")
