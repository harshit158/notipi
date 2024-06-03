## Installation
    $ pip install notipi 

## Setup
In order to use notipi library - you would be needing two environment variables: `BOT_API_TOKEN` and `CHAT_ID`

<u>To get `BOT_API_TOKEN`:</u>

- In the telegram app, initiate conversation with `@BotFather` and follow the instructions to create a new bot and get the `BOT_API_TOKEN`<br>
- You will be required to enter bot's account name and username.
- Detailed instructions can be found at [Telegram website](https://core.telegram.org/bots/features#creating-a-new-bot:~:text=and%20managing%20bots.-,Creating%20a%20new%20bot,-Use%20the%20/newbot)

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