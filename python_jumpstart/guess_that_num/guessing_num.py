import random

print("---------------------------")
print("  GUESS THAT NUMBER GAME")
print("---------------------------")
print()

the_num = random.randint(0, 100) # includes both as end points

guess = " "

while guess != the_num:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)

    if guess == the_num:
        print("Awesome, you got it!!")
    elif guess > the_num:
        print(f"{guess} is too high...!")
    elif guess < the_num:
        print(f"{guess} is too low...!")
    else:
        print("Are you sure you entered a number?")

print("---------------------------")
print("        DONE SON")
print("---------------------------")