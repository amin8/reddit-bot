import praw
import sys
import time

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = "<username>",
                password = "<password>",
                client_id = "ncoI2IWn-B0cOA",
                client_secret = "yFQINTI6OwuYw2TqqSMcUzN-u7Q",
                user_agent = "aminsbot private notifier v0.1")
    print "logged in!"

    return r

def get_usernames(filename):
    try:
        with open(filename, "r") as f:
            usernames = f.read()
            usernames = usernames.split("\n")
            usernames = filter(None, usernames)
    except IOError:
        print "Error: File " + filename + " was not found in the current directory"
        quit()

    return usernames

def send_message(r, username, subject, body):
    try:
        r.redditor(username).message(subject, body)
    except praw.exceptions.APIException as e:
        if "USER_DOESNT_EXIST" in e.args[0]:
            print "redditor " + username + " not found, did not send a message."
            return
    print "Sent message to " + username + "!"

if len(sys.argv) != 4 :
    print "usage: notifier_bot.py file \"subject\" \"body\""

print sys.argv[0]
print sys.argv[1]
print sys.argv[2]
print sys.argv[3]


filename = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

r = bot_login()
usernames = get_usernames(filename)
print usernames

for username in usernames:
    send_message(r, username, subject, body)
    time.sleep(5)
