from .bot import Bot


def main():
    bot = Bot()
    bot.get_users_by_hashtag_media('downhill')


if __name__ == "__main__":
    main()
