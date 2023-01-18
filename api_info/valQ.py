import requests


def get_val_info(username, tagline):
    print('hi')
    response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")
    data = response.json()['data']
    print(data)
    return data
    # print(data['elo'])

# def filter_info(data):
#     pass


# username = 'kelluu'
# tagline = 'comfy'

# response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")

# data = response.json()['data']

# print(data['currenttierpatched'])
# print(data)



