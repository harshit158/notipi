import os
import telegram
from telegram.ext import Updater
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def get_chat_id(token):
    bot = telegram.Bot(token=token)
    updates = await bot.get_updates()
    print(updates)
    for update in updates:
        print(update.message.chat.id)
  
async def send_msg(message):
    bot = telegram.Bot(os.environ['BOT_API_TOKEN'])
    async with bot:
        await bot.send_message(text=message, chat_id=os.environ['CHAT_ID'])
  
def notify(msg):
    try:
        os.environ['BOT_API_TOKEN'] and os.environ['CHAT_ID']
        asyncio.run(send_msg(msg))
    except KeyError:
        print('Please set BOT_API_TOKEN and CHAT_ID environment variables')