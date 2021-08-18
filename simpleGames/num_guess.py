# Creating a num guess game without looking anything up
# other than maybe documentation for the random library.
#
# 17 August 2021
#
import random

def guess_game():

    print("""
    -----------------------------
            WELCOME TO 
         GUESS THAT NUMBER
    -----------------------------
         """)

    num = random.randint(1, 100)

    username = input("What's your name? ")
    num_guesses = 0

    print(f"Good luck with guessing the number, {username}!  We've already determined the number....\n")
    print("... oh and we will be keeping track of the number of guesses you make. ;)\n")

    while True:
        guess = int(input("Give me any number between 1 and 100: "))

        if guess == num:
            print("That's right!! Awesome job there, sport.\n")
            num_guesses += 1
            if num_guesses > 1:
                print(f"Well, {username}, it seems like you figured it out in {num_guesses} tries... Not too shabby\n")
            else:
                print(f"Wow, {username}! You got it on your first try!\n")
            break
        elif guess > num:
            print("Too high! Try again\n")
            num_guesses += 1
        elif guess < num:
            print("Drat! That's too low! Try again...\n")
            num_guesses += 1


guess_game()
