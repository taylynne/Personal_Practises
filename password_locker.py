#! python3
# Just following along with the Automate the boring stuff python book

passwords = {'email': "F1mds957nsd*",
             'blog': 'ValMer52H4bA',
             'luggage': '4253',
             'facebook': 'Yri2NBsdn974'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python passwords.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to the clipboard.')
else:
    print("There is no account named " + account)

