import os
import telegram
from telegram.ext import Updater
import asyncio
from dotenv import load_dotenv
from functools import wraps
import argparse
import subprocess
import shlex
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

def run_cli(command_string):
    try:
        # Run the command
        command = shlex.split(command_string)
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Get the standard output, standard error, and return code
        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode

        # Print the results
        print("Standard Output:")
        print(stdout)
        print("Standard Error:")
        print(stderr)
        print("Return Code:", return_code)
        
        if return_code == 0:
            notify(f"Finished: {command_string}")
        else:
            notify(f"Error: {command_string}")

    except subprocess.CalledProcessError as e:
        # Handle errors in case the command failed
        display_string = f"An error occurred while running the command. {command_string}"
        print(display_string)
        notify(display_string)
        print("Error Output:", e.stderr)
        print("Return Code:", e.returncode)

def noticli():
    parser = argparse.ArgumentParser(description="Run a command and check its status.")
    parser.add_argument("-c", "--command", help="The command to run", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if not args.command:
        print("Please provide a command to run.")
        return
    
    run_cli(' '.join(args.command))

if __name__ == "__main__":
    noticli()