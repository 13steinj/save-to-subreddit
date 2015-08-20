import praw
from six.moves import input

# Python Reddit API Wrapper
# Python 2/3 Compatability library. If the user has PRAW,
# the user has six, as six is installed with PRAW

### USER CONFIGURATION ###
USERNAME = ""
PASSWORD = ""
SUBREDDIT = ""

# If LIMIT is < or = to 0, the amount will be the amount
# of posts you see in a page on your browser. If 'None'
# without quotes, it will do ALL saved posts. If > than
# 0 and < than 101, the amount will be that number.

LIMIT = 25

# If "botconfig.py" is in the folder or Python Library, the
# script will overwrite the above configuration with the
# equivalent variables in the module if the variable
# exists for ease of access, safety, and redistribution  

try:
    import botconfig
    USERNAME = botconfig.username
    PASSWORD = botconfig.password
    SUBREDDIT = botconfig.subreddit
except ImportError:
    pass
except AttributeError:
    pass


def main():
    r = praw.Reddit(user_agent = "save-to-subreddit")
    if USERNAME == "":
        USERNAME = input(">>Username: ")
    if PASSWORD == "":
        PASSWORD = input(">>Password: ")
    if SUBREDDIT == ""
        SUBREDDIT = input(">>Subreddit: ")
    USERNAME.replace("/u/", "")
    USERNAME.replace("/U/", "")
    USERNAME.replace("u/", "")
    USERNAME.replace("U/", "")
    SUBREDDIT.replace("/r/", "")
    SUBREDDIT.replace("/R/", "")
    SUBREDDIT.replace("r/", "")
    SUBREDDIT.replace("R/", "")
    USERAGENT = "Save-to-Subreddit by /u/alkorin"
    if USERNAME != "alkorin":
        USERAGENT += " in use by {0}".format(USERNAME)
    r = praw.Reddit(USERAGENT)
    r.login(USERNAME, PASSWORD)

    for post in r.get_me().get_saved(limit=LIMIT):

        post_name = str(post)

        try:
            semi = post_name.index(':')
            post_name = post_name[semi+2:]
        except Exception, CannotFind:
            pass

        sub = str(post.subreddit.display_name)
        package = '[' + sub + ']' + ' ' + post_name
        link = post.permalink
        print package
        r.submit(subreddit, package, url=link)
        post.unsave()

if __name__ == '__main__':
    main()
