# This is gonna be a bigger 'project'
# by that I just mean that I'm gonna work on it, and then develop it further as I go.
#
# Start date @ 29 July 2018


# First, set up rooms && the random generation of them.

import random


room1 = """\nAs you enter the dank musty room, a large rat scurries across the left exit. \
You swear that was the biggest rat you've ever seen, at least 50 kilos of pure muscle! \
Hopefully that was the only one, and there aren't any more in hiding waiting to get you... \
You really should've gone back for your weapons...
You see there are two exits: \n
A hallway to your left, and another hallway to your right.
"""

room2 = """\nThe room you arrive at can be described as is anything but clean... \n
There are old books torn to shreds; clothing, frayed and decaying, strewn all about; and \
unknown, undefinable objects that look better left untouched. There's even some sort of.. gooey substance \
draining from the bricks in the wall.  Gross.  It's probably better if you don't look up. \n
There is only one exit out of this horrible room: straight ahead through the worst of the mess.
"""

room3 = """\nThe smell of the room hits you first. And it isn't a pleasant one either... A mix of overriped \
fruit and rotten meat. \n
But what is emitting the smell, you're unsure.  There isn't a single object in this pristine looking room. \
It's probably best to get out of this room before the smell latches on you. (and before you lose your \
lunch)  There's three ways out: A long dark hallway straight ahead and doors to your right and left.
"""

room4 = """\nIf it wasn't for the sound of water dripping on the hard floor, you'd never know you entered \
a new room. It's that dark. Pitch black. You feel your eyes to make sure they are actually open. (they were) \
Hope there aren't any monsters in here... \n
You use your hands to follow along the wall to find a way out.  You count two: \n
Hallways to your right and straight.
"""

def ran_room():
    num = random.randint(1, 4)
    if num == 1:
        print(room1)
    elif num == 2:
        print(room2)
    elif num == 3:
        print(room3)
    elif num == 4:
        print(room4)
    else:
        print("Well... it seems we got lost.")

#ran_room()
# movement I suppose

def movement():
    while True:
        move = input("Which way do you want to go? ")
        if move.capitalize() == "L":
            print("You choose to go left and walk into the next room...")
            return
        elif move.capitalize() == "R":
            print("You choose to go right and walk into the next room...")
            return
        elif move.capitalize() == "S":
            print("You choose to go straight and walk into the next room...")
            return
        elif move.capitalize() == "Q":
            print("""You decide you cannot take any more of this and turn around to head back home... only you \
            don't remember which way you need to go to get back home.  As you start to panic, you realise every \
            room looks the same... you run.  You need to get out of here.  Now! \n
            
            You take a left, a right, you stumble over books... A rat squeaks and you scream.\n
            \n
            Calm. You try to calm yourself: 'You're the Grand Explorer Bruce. These Ruins are nothing for me. \
            Relax, and breathe. You will find your way out.' \n
            
            ... and you do. 2 days later.\n
            As you enter the room, you realise this is the same room you entered from. There's an ascending staircase \
            and there's light coming from up ahead! You run out, and decide you'd be better off staying a farmer...
            """)
        else:
            print("Please remember to use L, R, or S for movement. :)")

#movement()

# now to put it together...

entrance = """\nYou're the Grand Explorer Bruce! (At least, that's what you tell yourself...) \
You arrive at the entrance of the great Ruins of Martok, in hope for glory and loot.  Mostly loot. \
As you walk down the stairs to enter the Ruins, you realise that you managed to have forgotten all of your tools \
and weapons.  A chill runs down your back, and you sigh.  With all you said before you left, there's no going back \
even if it is for your gear. \n

The first room you enter is... clean and not decaying.  There doesn't seem to be any treasure here, but at least \
there are no monsters.  Well you're off to a good start at least! As you glance around the room you see you can \
exit to the next room via doors to your left, right, or straight ahead.
"""

print("""Welcome to the most basic of 'text' games -- if you can even call it that! \
Please use F, R, or L for movement. And you can enter 'q' whenever you want to quit! Good Luck!\n""")

print(entrance)

while True:
    movement()
    ran_room()

# Need to make it so it actually quits with Q
# pretty up the text