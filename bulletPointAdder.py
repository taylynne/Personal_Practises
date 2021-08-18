#! python3
# following along again with AtBS

import pyperclip

text = pyperclip.paste()

# TODO : Separate lines and add stars ~_~

new_text = text.split('\n')
for i in range(len(new_text)):          # loops through each line of the text
    new_text[i] = '* ' + new_text[i]    # adds a star to each line/string

text = '\n'.join(new_text)

pyperclip.copy(text)
