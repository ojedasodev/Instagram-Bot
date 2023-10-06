import sys
import config
from instagrapi import Client

cl = Client()

cl.login(config.ACCOUNT_USERNAME, config.ACCOUNT_PASSWORD)

try:

    user = cl.user_id_from_username("sagitario0588")  # get user info by username

    followers = cl.user_followers(
        user, amount=10).keys()  # Get followers by

    print(followers, file=open("followers.txt", "a"))
except Exception as e:
    print(e, file=open("error.log", "a"))
