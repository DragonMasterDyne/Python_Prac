# ClydeBank Coffee Shop Simulator 4000
# Copyright  (C) 2023 ClydeBank Media, All Rights Reserved

# Improt items from the random module to generate weather
import random

def welcom():   
    print(" Coffe Shop Simulator 400, Version 1.00")
    print(" Copyright  (C) 2023 ClydeBank Media, All Rights Reserved.\n")
    print(" Let's collect some information before we start the game.\n")

def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
    print("You have $" + str(cash_on_hand) + " cash on hand and the temperature is " + str(weather_temp) + ".")
    print("You have coffee on hand to make " + str(coffee_inventory) + " cups.\n")

def convert_to_float(s):
    # If conversion fails, assign 0 to it
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def x_of_y(x,y):
    num_list = []
    # Return a list of x copies of y
    for i in range(x):
        num_list.append(y)
    return num_list


class CoffeeShopSimulator:

    # Minimum  and maximum temperatures
    TEMP_MIN = 20
    TEMP_MAX = 90

    def __init__(self, player_name, shop_name):
        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name

        # Current day number
        self.day = 1

        # Cash on hand at start
        self.cash = 100.00

        # Inventory at start
        self.coffee_inventory = 100

        # Sales list
        self.sales = []

        # Possible temperatures
        self.tempa = self.make_temp_distrbution()

    def run(self):
        print("\nOk, let's get started. Have fun!")

        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text effect
            print("\n------| Day " + str(day) + " @ " + shop_name + " |-------")

            # Display the cash and weather
            temperature = self.weather

            # Display the cash and weather
            daily_stats(cash, temperature, coffee)

            # Get price of a cup of coffee 
            cup_price = prompt("What do you want to charge per cup of coffee? ")
    
            # Get advertising buddget
            print("\nYou can buy advertising to help promote sales.")
            advertising = prompt("How much advertising do you want to spend on advertising? (0 for none)?", False)

            # Convert advertising to float
            advertising = convert_to_float(advertising)

            # Deduct advertising from cash on hand
            cash -= advertising


def get_weather():
    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on, but this is good enough for now
    return randint(20,90)

# print welcome message
welcom()

# Get name and shop name

name = prompt("What is your name? ", True)
shop_name = prompt("What do you want to name your coffe shop?", True)

# We have what we need, so let's get started!
print("\nOk, let's get started, Have fun!")



    # TODO: calculate today's preformance
    # TODO: Display today's preformance

    # Before we loop around we add a day
    day += 1

    
# # Current day number
# day = 1

# # Starting cash on hand
# cash = 100.00

# # Coffee on hand
# coffee = 100


# # Sales list of dictionaries
# # sales = [
# #   {
# #       "day": 1,
# #       "coffee_inv": 100,
# #       "advertising": "10",
# #       "tem": 68,
# #       "cups_sold": 16
# #    },
# #    {
# #       "day": 2,
# #       "coffee_inv": 84,
# #       "advertising": "15",
# #       "tem": 72,
# #       "cups_sold": 20
# #    },
# #       "day": 1,
# #       "coffee_inv": 64,
# #       "advertising": "5",
# #       "tem": 78,
# #       "cups_sold": 10
# #    }
# # ]
# # Create an emty sales list
# sales = []

# # 