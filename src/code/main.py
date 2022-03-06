from instabot import Bot
from time import sleep
import schedule
from info import username, password

bot = Bot()
bot.login(username=username, password=password)

def post_pick():
  pass

schedule.every().day.at("19:00").do(post_pick)

while True:
  schedule.run_pending()
  sleep(1)