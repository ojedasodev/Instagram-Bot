from fastapi import FastAPI, BackgroundTasks

from .bot import Bot

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/followers/{ig_account}")
async def get_followers(ig_account: str):
    BackgroundTasks.add_task(get_followers, ig_account, Bot())
    return {"message": "U will get a notification when the bots ends"}
    
def get_followers(account: str, bot: Bot):
    followers = [ followers for followers in bot.get_followers()]
    print(followers)


   