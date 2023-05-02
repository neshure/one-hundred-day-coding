import random
from coffee_data import menu, resources
import time
import os



# Getting available resources
new_line = '\n'
water_available = resources["water"]
milk_available = resources["milk"]
coffee_available = resources["coffee"]


# Get latte data
latte_water_menu = int(menu["latte"]["ingredients"]['water'])
latte_milk_menu = int(menu["latte"]["ingredients"]['milk'])
latte_coffee_menu = int(menu["latte"]["ingredients"]['coffee'])
latte_cost = float(menu["latte"]["cost"])


 
# Get cappuccino data
cappuccino_water_menu = menu["cappuccino"]["ingredients"]['water']
cappuccino__milk_menu = menu["cappuccino"]["ingredients"]['milk']
cappuccino__coffee_menu = menu["cappuccino"]["ingredients"]['coffee']
cappuccino__cost = menu["cappuccino"]["cost"]


# Get espresso data 
espresso_water_menu = menu["espresso"]["ingredients"]['water']
espresso_coffee_menu = menu["espresso"]["ingredients"]['coffee']
espresso_cost = menu["espresso"]["cost"]

#Check for sufficient fund

def check_fund():
  add_fund = float(input('Please insert coin: $'))
  if (add_fund >= espresso_cost) or (add_fund >= cappuccino__cost) or (add_fund >= latte_cost):
    return add_fund
  else:
    is_fund_sufficient = True
    while is_fund_sufficient:
      if (add_fund < espresso_cost) or (add_fund < cappuccino__cost) or (add_fund < latte_cost):
        not_enough_fund = float(input('Insufficient fund. Please insert coin: $'))
        add_fund += not_enough_fund
      else:
        is_fund_sufficient = False
        return add_fund


# Turn the coffee maker on/off
turn_OnOff_coffee_maker = input("Type On/Off machine: ").lower()

if turn_OnOff_coffee_maker == 'off':
    print("Goodbye!")
    exit()
else:
    print('''
Coffee prices:
--------------

Espresso: $1.5
Latte: $2.5
Cappuccino: $3.0

''')
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    ask_user = input("Pick a drink latte/cappuccino/espresso or type report to display available resources: ").lower()
    while ask_user:
        if ask_user == "report":
          print(f'Available resources: {new_line} Water: {water_available}ml {new_line} Milk: {milk_available}ml {new_line} Coffee: {coffee_available}g ')
          ask_user = input("Pick a drink latte/cappuccino/espresso or type report to display available resources: ").lower()

        elif ask_user == "no":
           exit()

        elif ask_user == "espresso" and (water_available > espresso_water_menu) and (coffee_available > espresso_coffee_menu):
          water_available -= espresso_water_menu
          coffee_available -= espresso_coffee_menu
          enough_fund = check_fund()
          print("One moment.......")
          time.sleep(2)
          print(f"Take your change: ${enough_fund - espresso_cost}. Thank you!")
          print("Enjoy your drink")
          ask_user = input(f"Pick a drink latte/cappuccino/espresso {new_line}or{new_line}type report to display available resources {new_line}or{new_line}Type no to exit: ").lower()

        elif ask_user == "latte" and (water_available > latte_water_menu) and (milk_available > latte_milk_menu) and (coffee_available > latte_coffee_menu):
          water_available -= latte_water_menu
          milk_available -= latte_milk_menu
          coffee_available -= latte_coffee_menu
          enough_fund = check_fund()
          print("One moment.......")
          time.sleep(2)
          print(f"Take your change: ${enough_fund - latte_cost}. Thank you!")
          print("Enjoy your drink")
          ask_user = input(f"Pick a drink latte/cappuccino/espresso {new_line}or{new_line}type report to display available resources {new_line}or{new_line}Type no to exit: ").lower()

        elif ask_user == 'cappuccino' and (water_available > cappuccino_water_menu) and (milk_available > cappuccino__milk_menu) and (coffee_available > cappuccino__coffee_menu):
          water_available -= cappuccino_water_menu
          milk_available -= cappuccino__milk_menu
          coffee_available -= cappuccino__coffee_menu
          enough_fund = check_fund()
          print("One moment.......")
          time.sleep(2)
          print(f"Take your change: ${enough_fund - cappuccino__cost}. Thank you!")
          print("Enjoy your drink")
          ask_user = input(f"Pick a drink latte/cappuccino/espresso {new_line}or{new_line}type report to display available resources {new_line}or{new_line}Type no to exit: ").lower()

        else:
           if water_available < 250 or milk_available < 150 or coffee_available < 24:
              water_available = resources["water"]
              milk_available = resources["milk"]
              coffee_available = resources["coffee"]