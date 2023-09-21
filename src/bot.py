import sys
from instagrapi import Client
from config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD


class Bot():
    _cl = None

    def __init__(self):
        self._cl = Client()
        self._cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

    def get_users_by_hashtag_media(self, hashtag_name):
        try:
            medias = self.cl.hashtag_medias_top(
                'downhill', amount=1)  # Get hashtag ID by hashtag name
            return [self.cl.media_likers(media.pk) for media in medias]
        except Exception as e:
            print(sys.stderr, file=open("error.log", "a"))
            sys.exit(1)
