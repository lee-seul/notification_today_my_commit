# coding: utf-8


import os


secrets = {}
secret_path = os.path.join(os.path.dirname(__file__), 'secret.json')
if os.path.exists(secret_path):
    with open(secret_path) as f:
        secrets = json.loads(f.read())


def load_user_info(key):
    if key in secrets:
        return secrets[key]

