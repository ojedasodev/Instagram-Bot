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
                hashtag_name, amount=1)  # Get hashtag ID by hashtag name
            return [self.cl.media_likers(media.pk) for media in medias]
        except Exception as e:
            print(e, file=open("error.log", "a"))

    def get_followers(self, account_name: str):
        try:
            user = self.cl.user_info_by_username(
                account_name).dict()  # get user info by username

            followers = self.cl.user_followers(
                user["pk"]).keys()  # Get followers by

            return followers
        except Exception as e:
            print(e, file=open("error.log", "a"))

    @staticmethod
    def to_file(item):
        print(item, file=open("followers.txt", "a"))
