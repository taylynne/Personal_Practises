# I am just practising importing files for fun
# And I figured I'd use the "Zen of Python" as my test
# Cheers!
#
# 23 July 2018

file = 'zen_python.txt'

with open(file) as file_object:
    lines = file_object.readlines() # initially had .readline -- didn't know about this! This reads the first line

for line in lines:
    print(line.strip())

print('\n')
print(lines[2:4])






