from main import post_instagram, post_twitter
import sys
import os

def post_pic(new_day, platforms):
	if os.path.isfile("config/daily_monke_pic_uuid_and_cookie.json"):
		os.remove("config/daily_monke_pic_uuid_and_cookie.json")

		
	with open("../files/day.txt", "r") as f:
		day = int(f.read()) + new_day
	with open("../files/day.txt", "w") as f:
		f.write(str(day))

	caption = f"Day {day}"
	ig_caption = caption + " #spoonkid #dinkbot #blazed #monke #monkeclothing #funeemonkee #pietown #rust #majorbagalert #goomba #twitch #youtube"
	
	img_path = "../files/monke.jpg"

	print(f"Posting day {day}...")
	if platforms == "instagram" or platforms == "both":
		post_instagram(img_path, ig_caption)
	if platforms == "twitter" or platforms == "both":
		post_twitter(img_path, caption)

new_day = int(sys.argv[1])
platforms = sys.argv[2]

post_pic(new_day, platforms)