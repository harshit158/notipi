![PyPI - Downloads](https://img.shields.io/pypi/dm/notipi) ![PyPI - Version](https://img.shields.io/pypi/v/notipi)

<p align="center">
  <img src="assets/logo.png" alt="Logo" width="600"/>
</p>

## Installation
    $ pip install notipi 

## Setup
In order to use notipi library - you would be needing two environment variables: `BOT_API_TOKEN` and `CHAT_ID`

<u>To get `BOT_API_TOKEN`:</u>

- In the telegram app, initiate conversation with `@BotFather` (you can also click [here](https://t.me/BotFather)).
- Send `/newbot` as the message to `@BotFather` and provide a new name and username for your bot account as per the instructions.
- `@BotFather` will reply with a unique api token - this is your `BOT_API_TOKEN` <br>
(Note: Detailed instructions to create a new bot can be found at [Telegram website](https://core.telegram.org/bots/features#creating-a-new-bot:~:text=and%20managing%20bots.-,Creating%20a%20new%20bot,-Use%20the%20/newbot))

<p align="center">
  <img src="assets/bot_creation_steps.jpeg" alt="Logo" width="600"/>
</p>

<u>To get `CHAT_ID`:</u>
- Once a new bot is created, send a dummy message to the bot via Telegram app so that your chat gets assigned an ID. <br>
- Run the following script with your `BOT_API_TOKEN` to get your `CHAT_ID`
```python
from notipi.notipi import get_chat_id
get_chat_id(BOT_API_TOKEN)
```

This will give the following output:
```
Your CHAT ID: 1234567890
```

Once the `BOT_API_TOKEN` and `CHAT_ID` are obtained, set the environment variables

    export BOT_API_TOKEN=<bot_api_token>
    export CHAT_ID=<chat_id>

## Usage

Once the required environment variables are in place, following script can be used to send messages to your telegram app.

```python
from notipi.notipi import notify

def example():
    for i in range(1000):
        if i%100==0:
            notify(f"Currently at {i}")
```