# bot.py
import os
from dotenv import load_dotenv
import pandas as pd


import discord
from discord.ext import commands

from application.app import App
from updater import Updater


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

app = App()
bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())
updater = Updater(bot, app)

lolPlayers = pd.read_csv('players/lolPlayers.csv')['lol']
for p in lolPlayers:
    print(p)
    app.add_lol_acct(p)

valPlayers = pd.read_csv('players/valPlayers.csv')['val']
for p in valPlayers:
    user, tag = p.split('#')
    print(user, tag)
    app.add_val_acct(user, tag)

@bot.event
async def on_ready():
    await bot.add_cog(updater)
    
    channel = bot.get_channel(1065420015274315887)
    updater.channel = channel
    updater.lol_update.start()
    updater.val_update.start()


@bot.command()
async def status(ctx):
    msg = ''
    msg += 'LEAGUE\n'
    for name in app.lolAccts:
        msg += f'--{name}\n'
    msg += 'VALORANT\n'
    for name in app.valAccts:
        msg += f'--{name}\n'

    msg = 'Bot is up and running!\n' + msg
    msg = discord.Embed(description=f"""{msg}""")
    
    await ctx.send(embed=msg)

# @bot.command()
# async def add(ctx, game, userName):
#     event = None
    
#     if game.lower() == 'lol':
#         event = app.add_lol_acct(userName) 

#     response = get_output(event)
#     await ctx.send(response)


# @bot.command()
# async def show(ctx, game, userName=None):
#     event = None

#     if game.lower() == 'lol':
#         if userName is None:
#             event = app.get_lol_accts()
#         else:
#             event = app.get_lol_acct(userName) 
#     else:
#         return

#     response = get_output(event)
#     await ctx.send(response)




# @bot.command()
# async def helpme(ctx):
#     response = get_output(Commands())
#     await ctx.send(embed=response)


bot.run(TOKEN)


