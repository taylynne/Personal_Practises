# Making a script to move image files from my downloads folder to
# my image folder
#
#
# FOLLOW UP IDEA now that it works
# make it accept user input
# asking where to move to (and from where)
# and perhaps what file type as well

import os

os.chdir('C://Users/Justine/Downloads')

for f in os.listdir():
    file_name, file_exe = os.path.splitext(f)

    if file_exe == '.jpg' or file_exe == '.png':
        print(file_exe)
        os.rename("C://Users/Justine/Downloads/{}{}".format(file_name, file_exe),
                  "C://Users/Justine/Pictures/moved/{}{}".format(file_name, file_exe))
    else:
        pass
