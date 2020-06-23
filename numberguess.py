import random

x = random.randint(1, 10)
guess = input("Guess a number from 1 and 10: ")
try:
    if int(guess) > 0 and int(guess) < 11:
        if int(guess) == x:
            print("You got it!")
        else:
            print("The number was {}, please play again.".format(x))
    else:
        print("Please enter a number from 1 to 10")
except TypeError:
    print("Please enter a valid number")


y = random.choice([11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20])
list_guess = input("Guess a number from 11 to 20: ")
try:
    if int(list_guess) > 11 and int(list_guess) < 20:
        if int(list_guess) == y:
            print("you got it!")
        else:
            print("The number was {}, please try again.".format(y))
    else:
        print("Please enter a number from 11 to 20")
except TypeError:
    print("Please enter a valid number")
