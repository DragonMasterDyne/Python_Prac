from random import seed
from random import randint

number = randint(10,100)
print(number)
print("Welcome to the numbers game!\nCan you guess the number between 10 and 100?")
guess = input("What is your guess!?!?!?!?! ")
while guess != number:
    over = int(guess) - number
    under = number - int(guess)
    print(guess)
    if int(guess) == number:
                print("Your did it")
                break   
    elif under > 0:
            if under > 30 :
                print("Not even close too low")
                print(str(under) + " off")
                guess = input("What's your new guess? ")
            elif under > 15 & under <= 29:
                print("Soooo close too low")
                print(str(under) + " off")
                guess = input("What's your new guess ")
            elif under < 15:
                print("Keep going so close! Too low.")
                print(str(under) + " off")
                guess = input("What's your new guess? ")
    else:
            if over > 30:
                print("Waaaaay tooo high")
                print(str(over) + " off")
                guess = input("What's your new guess? ")
            elif over > 15 & over <= 29:
                print("Almost too high tho")
                print(str(over) + " off")
                guess = input("What's your new guess? ")
            elif over < 15:
                print("Missed it by that much! Too high.")
                print(str(over) + " off")
                guess = input("What's your new guess? ")