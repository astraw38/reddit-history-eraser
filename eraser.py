"""
Pass in user name (and password retrieved via envvars or getpass), will erase all but the last week of history.
"""
import argparse
import os
import sys
from getpass import getpass

import praw

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USER_AGENT = "{}:reddit-history-eraser:0.1".format(sys.platform)


def edit_post():
    """
    :return:
    """


def delete_post():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    args = parser.parse_args()
    password = getpass("Enter Reddit password")

    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         password=password,
                         username=args.username)

    print(reddit.user.me())
