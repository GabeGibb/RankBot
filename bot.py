# bot.py
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from discord_io.handle_output import *
from application.events import *
from application.app import App

from repeater import Repeater

import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

app = App()
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
rep = Repeater(bot, app)

players = pd.read_csv('players.csv')['lol']

for p in players:
    print(p)
    app.add_lol_acct(p)


@bot.event
async def on_ready():
    await bot.add_cog(rep)
    
    channel = bot.get_channel(963660571029417996)
    rep.channel = channel
    rep.get_data.start()


# @bot.command()
# async def add(ctx, game, userName):
#     event = None
    
#     if game.lower() == 'lol':
#         event = app.add_lol_acct(userName) 

#     response = get_output(event)
#     await ctx.send(response)


@bot.command()
async def show(ctx, game, userName=None):
    event = None

    if game.lower() == 'lol':
        if userName is None:
            event = app.get_lol_accts()
        else:
            event = app.get_lol_acct(userName) 

    response = get_output(event)
    await ctx.send(response)


@bot.command()
async def helpme(ctx):
    response = get_output(Commands())
    await ctx.send(embed=response)


bot.run(TOKEN)

