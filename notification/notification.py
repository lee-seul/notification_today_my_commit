# coding: utf-8 


import requests

from response import get_push_event_json, get_event_list
try:
    from secret import *
except:
    from config import *


def send_message(bot_key=BOT_API_KEY, channel=MY_CHANNEL_NAME):
    count = len(get_push_event_json(get_event_list()))
    text = f'today commit {count}'
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={channel}&text={text}'
    response = requests.get(url)


if __name__ == '__main__':
    send_message()
