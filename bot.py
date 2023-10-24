from .models.User import User
from instagrapi import Client
from .npltokens import ENG_TOKENS, SPA_TOKENS
import spacy

from .config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD


class InstagramBot():
    _cl = Client()
    _lang = None

    def __init__(self, lang: str):
        self._lang = lang
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
            userid = self.cl.user_id_from_username(account_name)

            followers = self.cl.user_followers(
                userid).keys()  # Get followers by

            for user in followers:
                yield self.user_info(user)

        except Exception as e:
            print(e, file=open("error.log", "a"))

    def user_info(self, userId: str) -> User:
        try:

            user = self.cl.user_info(userId)
            return User(
                username=user["username"],
                full_name=user["full_name"],
                is_private=user["is_private"],
                is_verified=user["is_verified"],
                media_count=user["media_count"],
                follower_count=user["follower_count"],
                is_business=user["is_business"],
                # tambien buscar por otras fuentes
                biography=user["biography"],
                interests=self.get_interests(user["biography"])
            )
        except Exception as e:
            print(e)

    def get_interests(self, biography: str):
        interests = []
        nlp = spacy.load("en_core_web_sm") if self._lang == "EN" else spacy.load(
            "es_core_news_sm")
        token_set = ENG_TOKENS if self._lang == "EN" else SPA_TOKENS
        document = nlp(biography)

        for token in document:
            if token.text in token_set:
                interests.append(token.text)

        return interests
