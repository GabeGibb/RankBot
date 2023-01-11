
from discord.ext import commands, tasks

import time as t


class Repeater(commands.Cog):
    def __init__(self, bot, app):
        self.bot = bot
        self.app = app
        self.running = False


    @commands.command()
    async def start(self, ctx):
        if self.running:
            return
        self.ctx = ctx
        self.running = True
        self.get_data.start()



    @tasks.loop(seconds=3.0)
    async def get_data(self):
        if not self.running:
            return

        for key, value in self.app.lolAccts.items():
            if value.prevInfo == value.info:
                await self.ctx.send(f'{key} same')

          
    @commands.command()
    async def stop(self, ctx):
        self.running = False


  