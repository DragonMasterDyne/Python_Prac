# Input is a built in function that prints a string and then takes an input form the user. The input is strored and returned as a string.
price = input("What is the price of a cup of coffee? ")
cups = input("How many cups do you want? ")
total = float(price) * int(cups)
# print is another built in function that prints a string into the terminal. Only excepts strings.
print("Your total is $" + str(total) + " for " + cups + " cups.") 