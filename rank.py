import requests



# username = input()
# tagline = input()

# username = 'racecarjoe'
# tagline = 'NA1'

# response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")

# data = response.json()['data']

# print(data['currenttierpatched'])



RIOT_KEY='RGAPI-4dd65fa6-eac6-475a-ad00-364d912a13cd'
user = 'BlueNarwhal'

response  = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={RIOT_KEY}').json()

id = response['id']

response1 = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={RIOT_KEY}').json()

# print(response1[1]['tier'], response1[1]['rank'])
# print(response1)
for r in response1:
    print(r['queueType'], r['tier'], r['rank'])
