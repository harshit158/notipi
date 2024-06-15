import os
if not os.environ.get('BOT_API_TOKEN') and not os.environ.get('CHAT_ID'):
    print(f'Notipi: Please set these env variables: [BOT_API_TOKEN, CHAT_ID] to receive notifications on Telegram. \nNotifications will now be sent only via mac')