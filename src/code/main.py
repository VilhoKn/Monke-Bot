from instabot import Bot
from time import sleep
import schedule
from info import username, password

bot = Bot()
bot.login(username=username, password=password)

def post_pick():
  with open("../files/day.txt", "r") as f:
    day = int(f.read()) + 1
  with open("../files/day.txt", "w") as f:
    f.write(str(day))

  caption = f"Day {day} #spoonkid #dinkbot #blazed #monke #monkeclothing #funeemonkee #pietown #rust #majorbagalert #goomba #twitch #youtube"
  
  image_path = "../files/monke.jpg"

  bot.upload_photo(image_path, caption=caption)
  print("Tried to upload pic")
  
  if bot.api.last_response.status_code != 200:
    print(f"Error: {bot.api.last_response}")
  else:
    print("Pic was uploaded successfully")
    

schedule.every().day.at("19:00").do(post_pick)

while True:
  schedule.run_pending()
  sleep(1)