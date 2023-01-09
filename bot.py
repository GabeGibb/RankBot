# bot.py
import os

import discord
from dotenv import load_dotenv
from discord_io.handle_msg import *
from discord_io.handle_output import *
from application.app import App

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())
app = App()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    event = decide_command(message)
    execute_output(event)
    


client.run(TOKEN)