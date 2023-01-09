# bot.py
import os

import discord
from dotenv import load_dotenv

from app import App
# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client(intents=discord.Intents.all())

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('hi rank')


# client.run(TOKEN)

def main():
    a = App()
    a.create_person()
    


if __name__ == '__main__':
    main()
