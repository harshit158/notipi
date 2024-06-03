import os
import telegram
from telegram.ext import Updater
import asyncio
from dotenv import load_dotenv
from functools import wraps
load_dotenv()

def async_decorator(f):
    """Decorator to allow calling an async function like a sync function"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        ret = asyncio.run(f(*args, **kwargs))

        return ret
    return wrapper

@async_decorator
async def get_chat_id(token: str):
    bot = telegram.Bot(token=token)
    updates = await bot.get_updates()
    if len(updates)==0:
        print('Updates not found. Try sending a dummy message to your bot.')
    print(f'Your CHAT ID: {updates[0].message.chat.id}')
  
async def send_msg(message):
    bot = telegram.Bot(os.environ['BOT_API_TOKEN'])
    async with bot:
        await bot.send_message(text=message, chat_id=os.environ['CHAT_ID'])
  
def notify(msg: str):
    try:
        os.environ['BOT_API_TOKEN'] and os.environ['CHAT_ID']
        asyncio.run(send_msg(msg))
    except KeyError:
        print('Please set BOT_API_TOKEN and CHAT_ID environment variables')