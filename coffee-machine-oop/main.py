from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_make=CoffeeMaker()
money_machine=MoneyMachine()
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=='report':
        coffee_make.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_make.make_coffee(drink)
