# trying out some tweeter bot stuff

import tweepy, time, sys

argfile = str(sys.argv[1]) # argv[0] is this .py file; argv[1] is a txt file with the same name - is it always a txt file?

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile,'r') # opens and reads the file
f = filename.readlines() # saves the lines in the document as f
filename.close() # closes the document, no longer usable by the rest program

for line in f: # this is where the 'magic' happens (to quote the tutorial); loops through each line in f (the 'new' file)
    api.update_status(status=line)
    time.sleep(900) # this sets up tweets for every 15 minutes; tells the bot to 'sleep' for 900 seconds

