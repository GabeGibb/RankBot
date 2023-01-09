from requests import get

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('RIOT_KEY')

RIOT_KEY=TOKEN

def find_lol_id(user):
    response  = get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={RIOT_KEY}').json()
    return response['id']

def get_lol_info(id):
    response = get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={RIOT_KEY}').json()
    return choose_lol_info(response)


def choose_lol_info(data):
    dict = {}
    keepData = ['tier', 'rank', 'leaguePoints', 'wins', 'losses']


    for d in data:
        attrDict = {}
        mode = d['queueType']
        
        for attr in d:
            if attr in keepData:
                attrDict[attr] = d[attr]

        dict[mode] = attrDict
    
    return dict



