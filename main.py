from fastapi import FastAPI, BackgroundTasks

from bot import InstagramBot

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Instagram bot service"}


@app.get("/followers/{ig_account}/{lang}")
async def get_followers(ig_account: str, lang: str):
    BackgroundTasks.add_task(get_followers, ig_account,
                             InstagramBot(lang=lang.capitalize()))
    return {"message": "You will get a notification when the bots ends"}


def get_followers(account: str, bot: InstagramBot):
    followers = [
        followers.__dict__ for followers in bot.get_followers(account)]

    # send result to client via webhook.
    print(followers)
