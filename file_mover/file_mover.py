# Script to move files from one location to another
# asks user:
# file type to be moved
# location to start at
# location to move files to
#
# eventually  maybe use UI to make it easier.
#

import os


questions = open("questions.txt").read().splitlines()

where_from, where_to, file_types = questions

def location_converter(lct):
    # converts backslashes to forwardslashes

    lct = lct.replace("\\", "/")
    return lct

def file_location_start():
    # asks user for start location

    start = input(where_from + "\n")
    start = location_converter(start)
    return start

def file_location_end():
    # asks user for end location

    end = input(where_to + "\n")
    end = location_converter(end)
    return end

def file_type():
    # asks for file type and verifies it is a valid file type
    # makes sure the file type has a "."

    valid_file_types = [
        "jpg", ".jpg", ".png", "png",
        "txt", ".txt", "exe", ".exe",
        ".doc", "doc", "docx", ".docx",
        "pdf", ".pdf", "zip", ".zip",
        "mobi", ".mobi", 'epub', '.epub',
        "gif", '.gif',
    ]

    f_type = ""
    while f_type not in valid_file_types:
        f_type = input(file_types + "\n")
        f_type = f_type.strip()
        if f_type in valid_file_types:
            if f_type[0] == ".":
                return f_type
            else:
                f_type = "." + f_type
                return f_type
        else:
            print("Sorry that's not a valid file type.")

def print_intro():
    with open("intro.txt", 'r') as f_obj:
        print(f_obj.read())
    print("\n")

def actual_program():
    # I guess this part actually does the magic of the program so to speak

    start_loc = file_location_start()
    end_loc = file_location_end()
    f_extension = file_type()

    for f in os.listdir(start_loc):
        file_name, file_exe = os.path.splitext(f)

        if file_exe == f_extension:
            print(file_name)
            # so, thinking about this, I may need to check the locations and
            # make sure they do not have a "/" at the end - so it doesn't potentially
            # crash the script.  Might be nice to create the directory if it doesn't
            # exist as well.
            os.rename(
                f"{start_loc}/{file_name}{f_extension}",
                f"{end_loc}/{file_name}{f_extension}"
            )
        else:
            pass


print_intro()
actual_program()
