# coding: utf-8 


import requests
import datetime

try:
    from secret import *
except:
    from config import *


def get_event_list(user_name=USERNAME, token=API_TOKEN):
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/users/{user_name}/events'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return None 


def parse_time_data(created_at):
    created_at = created_at.split('T')
    return created_at[0].split('-')


def parse_today_commit_data(data):
    now = datetime.datetime.utcnow()
    year = now.year
    month = now.month
    day = now.day
    
    result = []
    created_at = list(map(int, parse_time_data(data['created_at'])))
    if created_at[0] == year and created_at[1] == month and created_at[2] == day:
        result.append(data['payload']['commits'])
    return result


def get_push_event_json(json_response):
    result = []    
    for data in json_response:
        if data['type'] == 'PushEvent':
            commit = parse_today_commit_data(data)
            if commit:
                result.append(commit)
    return result

