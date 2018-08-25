# Just messing around
# making a guess the numbers "game"
# 25 July 2018

import random

def generatedNum():

    opt_one = int(input("What is the number you'd like to start from? "))
    opt_two = int(input("What is the number you'd like it to end with? "))

    return random.randint(opt_one, opt_two)

def random_game(num):
    guess = int(input("What is your guess? "))
    tries = 0

    while guess != num:
        if guess > num:
            print("Too high!")
            guess = int(input("Guess again! "))
            tries += 1
        elif guess < num:
            print("Too low!")
            guess = int(input("Guess again! "))
            tries += 1

    print("\nYou guessed it!")
    print("The number was " + str(num))
    print("And you guessed it in " + str(tries) + " tries!")


num = random.randint(1, 20)

print("Let's play a game of guess the number! Guess what number I'm thinking of, between 1 and 20")

random_game(num)

print("Now let's play a new game where you pick the range! \n")
new_num = generatedNum()
random_game(new_num)

while True:  # Maybe try to update this so that it asks if you want to pick a new range or not. can be tedious otherwise
    endless = input("Want to play another round? Y or N ")
    if endless.capitalize() == "Y":
        new_num = generatedNum()
        random_game(new_num)
    elif endless.capitalize() == "N":
        break




