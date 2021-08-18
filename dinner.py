import random

#what to eat for dinner.

print("In your mind, assign a number to each choice; or write it down whatever you want to do.")
num_option = int(input('How many choices are there? '))


decision = random.randint(1, num_option)

print("The decisions is... " + str(decision))
input("Sorry if you lost... press enter to exit.")