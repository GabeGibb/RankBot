import requests

# username = input()
# tagline = input()

username = 'racecarjoe'
tagline = 'NA1'

response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")

data = response.json()['data']

print(data['currenttierpatched'])


