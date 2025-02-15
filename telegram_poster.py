import os
import random
import telegram
import schedule
import time
from telegram.error import TelegramError

# Replace with our bot token and chat ID
BOT_TOKEN = 'TOKEN_BOT'
CHAT_ID = 'CHAT_ID'
IMAGES_PATH = 'images/'
HIDE_PATH = 'images/'

# Function to post in Telegram
def telegrampost(media, photocaption):
    bot = telegram.Bot(token=BOT_TOKEN)
    try:
        bot.send_photo(chat_id=CHAT_ID, photo=open(media, 'rb'),
        caption=photocaption)
        # print(f"Posted: {photocaption}")
    except TelegramError as e:
        # print(f"Failed to post: {e}")
        print(e)

# Function to pick a random file
def randomfile():
    files = [os.path.join(path, filename)
    for path, dirs, files in os.walk(IMAGES_PATH)
    for filename in files
    if (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG"))]
    return random.choice(files)

# Function to post a random image
def post_random_image():
    postitem = randomfile()
    chatcaption = postitem.replace(HIDE_PATH, '')
    telegrampost(postitem, chatcaption)

# Schedule posts
schedule.every().day.at("00:00").do(post_random_image)
schedule.every().day.at("01:00").do(post_random_image)
schedule.every().day.at("09:00").do(post_random_image)
schedule.every().day.at("10:00").do(post_random_image)
schedule.every().day.at("11:00").do(post_random_image)
schedule.every().day.at("12:00").do(post_random_image)
schedule.every().day.at("13:00").do(post_random_image)
schedule.every().day.at("14:00").do(post_random_image)
schedule.every().day.at("15:00").do(post_random_image)
schedule.every().day.at("16:00").do(post_random_image)
schedule.every().day.at("17:00").do(post_random_image)
schedule.every().day.at("18:00").do(post_random_image)
schedule.every().day.at("19:00").do(post_random_image)
schedule.every().day.at("20:00").do(post_random_image)
schedule.every().day.at("21:00").do(post_random_image)
schedule.every().day.at("22:00").do(post_random_image)
schedule.every().day.at("23:00").do(post_random_image)

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)


