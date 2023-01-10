# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_io.handle_output import *
from application.app import App

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


app = App()
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())



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

bot.run(TOKEN)
