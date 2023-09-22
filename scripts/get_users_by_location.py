import sys
from instagrapi import Client
from config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD

""" 
This script will:
1. Login
2. Get top media by location 
3. Get users liked the media

Instagrapi do not have a method to get users by location, so we need to
get the media by location and then get the users who liked the media.
"""

try:
    cl = Client()
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)  # Login to Instagram account

    """
    on this line, we get the top media by location
    """
    medias = cl.location_medias_top(
        '213385402', amount=1)  # Get hashtag ID by hashtag name

    """
    to ritrieve the users, we need to get the media id from the hashtag
    and then think about a way to get the users from the media.

    can use media_likers(media_id: str) to get the users who liked the media
    """

    media_likers = [cl.media_likers(media.pk) for media in medias]

    print(media_likers, file=open("media_likers_loc.txt", "a"))
    sys.exit(0)
except Exception as e:
    print(str(sys.stderr), file=open("error.log", "a"))
    sys.exit(1)
