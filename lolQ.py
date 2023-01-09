from requests import get

RIOT_KEY='RGAPI-4dd65fa6-eac6-475a-ad00-364d912a13cd'

def find_lol_id(user):
    response  = get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={RIOT_KEY}').json()
    return response['id']

def get_rank_info(id):
    response = get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={RIOT_KEY}').json()
    
    for r in response:
        print(r['queueType'], r['tier'], r['rank'])