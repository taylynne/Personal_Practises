# expanding on move_imgs
# asks what file type someone wants to move
# and the directory to move the files to

import os

# how many file types someone wants to move
num_f_types = int(input("Would you like to move one or two file types at once?\n"))

# loop to go accept the file types
if num_f_types == 1:
    f_type = input("What is the one file type you want to move?\n")
elif num_f_types == 2:
    f_type = [input("What is the first file type you want to move?\n")]
    f_type.append(input("What is the second file type you would like to move?\n"))
else:
    print("Sorry that number is not supported currently")

# What directory would the user like to move from
first_dir = input("What is the directory you would like to move files from (exact location)\n")
first_dir = first_dir.replace("\\", "/")

# Directory to move to
second_dir = input("And where would you like the files to be moved to?\n")
second_dir = second_dir.replace("\\", "/")
