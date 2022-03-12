from instabot import Bot
from time import sleep
import schedule
import tweepy
from info import *

import os
if os.path.isfile("config/daily_monke_pic_uuid_and_cookie.json"):
    os.remove("config/daily_monke_pic_uuid_and_cookie.json")

bot = Bot()
bot.login(username=username, password=password)

def post_pic():
  with open("../files/day.txt", "r") as f:
    day = int(f.read()) + 1
  with open("../files/day.txt", "w") as f:
    f.write(str(day))

  caption = f"Day {day}"
  ig_caption = caption + " #spoonkid #dinkbot #blazed #monke #monkeclothing #funeemonkee #pietown #rust #majorbagalert #goomba #twitch #youtube"
  
  img_path = "../files/monke.jpg"

  print(f"Posting day {day}...")
  post_instagram(bot, img_path, ig_caption)
  post_twitter(img_path, caption)


def post_instagram(bot, img_path, caption):
  bot.upload_photo(img_path, caption=caption)
  print("Tried to upload pic to instagram")

  if bot.api.last_response.status_code != 200:
    print(f"Instagram Error: {bot.api.last_response}")
  else:
    print("Pic was uploaded successfully to instagram" )


def post_twitter(img_path, caption):
  authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
  authenticator.set_access_token(access_token, access_token_secret)

  api = tweepy.API(authenticator, wait_on_rate_limit=True)

  media = api.media_upload(img_path)
  api.update_status(status=caption, media_ids=[media.media_id])
  
  print("Tried to upload pic to twitter")


schedule.every().day.at("21:00").do(post_pic)

while True:
  schedule.run_pending()
  sleep(1)
