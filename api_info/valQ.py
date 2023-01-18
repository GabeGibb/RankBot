import requests


def get_val_info(username, tagline):
    response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")
    data = response.json()['data']
    return data



