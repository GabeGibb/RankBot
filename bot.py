# bot.py
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from discord_io.handle_output import *
from application.events import *
from application.app import App

from repeater import Repeater

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

app = App()
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
rep = Repeater(bot, app)

@bot.event
async def on_ready():
    await bot.add_cog(rep)

    
@bot.command()
async def add(ctx, game, userName):
    event = None
    
    if game.lower() == 'lol':
        event = app.add_lol_acct(userName) 

    response = get_output(event)
    await ctx.send(response)


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

