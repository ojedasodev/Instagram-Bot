import sys
from instagrapi import Client
from config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD

""" 
This script will:
1. Login
2. Get hashtag ID
3. Get users by hashtag ID

this is the inicial aproach, but it's not working.
because the hashtag_medias_top() only returns top.
media listed for the hastag, not the users.
"""

try:
    cl = Client()
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)  # Login to Instagram account

    """
    on this line, we get the hashtag top medias by hashtag name
    """
    medias = cl.hashtag_medias_top(
        'downhill', amount=1)  # Get hashtag ID by hashtag name

    """
    to ritrieve the users, we need to get the media id from the hashtag
    and then think about a way to get the users from the media.

    can use media_likers(media_id: str) to get the users who liked the media
    """

    media_likers = [cl.media_likers(media.pk) for media in medias]

    print(media_likers, file=open("media_likers.txt", "a"))
    sys.exit(0)
except Exception as e:
    print(sys.stderr, file=open("error.log", "a"))
    sys.exit(1)
