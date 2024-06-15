import os
import telegram
from telegram.ext import Updater
from dotenv import load_dotenv
from functools import wraps
import argparse
import subprocess
import shlex
from .utils import require_envs, async_decorator, is_notebook
import asyncio
import nest_asyncio
from typing import Optional, Callable, Union
from notipi.notify_macos import display_notification

@async_decorator
async def get_chat_id(token: str):
    bot = telegram.Bot(token=token)
    updates = await bot.get_updates()
    if len(updates)==0:
        print('Updates not found. Try sending a dummy message to your bot.')
    print(f'Your CHAT ID: {updates[0].message.chat.id}')

def send_macos_msg(message: str):
    display_notification(message, title="Notipi")

async def send_msg(message: str):
    bot = telegram.Bot(os.environ['BOT_API_TOKEN'])
    async with bot:
        await bot.send_message(text=message, chat_id=os.environ['CHAT_ID'])

@require_envs('BOT_API_TOKEN', 'CHAT_ID')
def notify(arg: Optional[Union[Callable, str]] = None):
    if callable(arg):
        # If used as a decorator : @notify
        @wraps(arg)
        def wrapper(*args, **kwargs):
            result = arg(*args, **kwargs)
            message = f'Finished executing: {arg.__name__}'
            send_macos_msg(message)
            
            # Proceed only if Telegram is to be used
            if eval(os.environ.get('SEND_TO_TELEGRAM')):
                if is_notebook():
                    loop = asyncio.get_event_loop()
                    if loop.is_running():    
                        asyncio.ensure_future(send_msg(message))  # Schedule the coroutine
                    else:
                        loop.run_until_complete(send_msg(message))
                else:
                    asyncio.run(send_msg(message))
            return result
        return wrapper
    else:
        # If used as a standalone function: notify(msg)
        arg = 'Finished Task' if arg is None else arg
        send_macos_msg(arg)
        
        # Proceed only if Telegram is to be used
        if eval(os.environ.get('SEND_TO_TELEGRAM')):
            if is_notebook():
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    return asyncio.ensure_future(send_msg(arg))  # Schedule the coroutine
                else:
                    loop.run_until_complete(send_msg(arg))
            else:
                asyncio.run(send_msg(arg))

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

@require_envs('BOT_API_TOKEN', 'CHAT_ID')
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