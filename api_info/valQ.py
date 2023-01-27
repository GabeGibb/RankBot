from requests import get

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('VAL_KEY')

def get_val_info(username, tagline):
    headers = {'Authorization': TOKEN}
    response = get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}", headers=headers)
    data = response.json()['data']
    return data


# print(get_val_info('kachatakoowl', 'NA1'))