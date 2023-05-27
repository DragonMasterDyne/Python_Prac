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

            # Get the weather
            temperature = self.weather

            # Display the cash and weather
            self.daily_stats(temperature)

            # Get price of a cup of coffee 
            cup_price = float(prompt("What do you want to charge per cup of coffee? "))
    
            # Get advertising buddget
            print("\nYou can buy advertising to help promote sales.")
            advertising = prompt("How much advertising do you want to spend on advertising? (0 for none)?", False)

            # Convert advertising to float
            advertising = convert_to_float(advertising)

            # Deduct advertising from cash on hand
            self.cash -= advertising

            # Simulate today's sales
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price

            # Display the results
            print("You sold " + str(cups_sold) + " cups of coffee today.")
            print("You make $" + str(gross_profit) + ".")

            # Addthe profit to our coffers
            self.increment_day()
    
    def simulate(self, temperature, advertising, cup_price):
        # Find out hom many cups were sold
        cups_sold = self.daily_sales(temperature, advertising)

        # Save the data for today
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })

        # We technically don't need this, but why make the next step
        # read from the sales list when we have the data right here
        return cups_sold
    
def make_temp_distribution(self):
    # This is not a good bell curve, but it will do for now
    # until we get to more advanced mathematice
    temps= []

    # First, find the average between TEMP_MIN and TEMP_MAX
    avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
    # Find the distance between TEMP_MAX and the average
    max_dist_from_avg = self.TEMP_MAX - avg

    # Loop through all possible temperatures
    for i in range(self.TEMP_MIN, self.TEMP_MAX):
        # How far away is the temperature from average?
        # abs() gives us the absolute value
        dist_from_avg = abs(avg - i)
        # How far away is the dist_from_avg from the maxium
        # This will be lower for temps at the extrems
        dist_from_max_dist = max_dist_from_avg - dist_from_avg
        # If the value is zero, make it one
        if dist_from_max_dist == 0:
            dist_from_max_dist = 1
        # Append the output of x_of_y to temps
        for t in x_of_y(int(dist_from_max_dist), i):
            temps.append(t)
        return temps



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