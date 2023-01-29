
import discord
from discord.ext import commands, tasks
from asyncio import sleep
from random import choice

class Updater(commands.Cog):
    def __init__(self, bot, app):
        self.bot = bot
        self.app = app
        self.channel = None

    @tasks.loop(seconds=90.0)
    async def val_update(self):
        for key, value in self.app.valAccts.items():
            await sleep(0)
            try:
                value.set_info()
                prev = value.prevInfo
                cur = value.info
                
                msg = ''
                if prev['elo'] == cur['elo']:
                    continue
                
                change = cur['elo'] - prev['elo']
                if prev['currenttierpatched'] != cur['currenttierpatched']:
                    if change > 0:
                        msg = f'{key} just promoted to {cur["currenttierpatched"]}'
                    else:
                        msg = f'{key} just demoted to {cur["currenttierpatched"]}'
                
                else:
                    if change > 0:
                        msg = f'{key} just gained {cur["mmr_change_to_last_game"]}RR'
                    else:
                        msg = f'{key} just lost {abs(cur["mmr_change_to_last_game"])}RR'
                
                if key in ('DARKCHERIZARD', 'erinn', 'ATTACK ATTACK'):
                    if change > 0:
                            msg += f'\n{self.get_winsult()}'
                    else:
                        msg += f'\n{self.get_losesult()}'
                print(msg)
                botMsg = discord.Embed(description=f"""VALORANT RANKED\n{msg}""", color=0xfa4454)
                await self.channel.send(embed=botMsg)
            except Exception as e:
                print(key, e)



    @tasks.loop(seconds=90.0)
    async def lol_update(self):
        lolDict = {'IRON': 0, 'BRONZE': 1, 'SILVER': 2, 'GOLD': 3, 'PLATINUM': 4, 'DIAMOND': 5, 'MASTER': 6, 'GRANDMASTER': 7, 'CHALLENGER': 8}
        numDict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}

        for key, value in self.app.lolAccts.items():
            await sleep(0)
            try:
                value.set_info()
            
                for p, c in zip(value.prevInfo.items(), value.info.items()):
                    mode = c[0]
                    prev = p[1]
                    cur = c[1]
                    if prev['wins'] == cur['wins'] and prev['losses'] == cur['losses']:
                        continue

                    msg = ''
                    rankChange = False

                    if prev['tier'] != cur['tier']:
                        pRank = lolDict[prev['tier']]
                        cRank = lolDict[cur['tier']]
                        change = cRank - pRank
                        rankChange = True 

                    elif prev['rank'] != cur['rank']:
                        change = numDict[cur['rank']] - numDict[prev['rank']]
                        rankChange = True

                    elif prev['leaguePoints'] != cur['leaguePoints']:
                        change = cur['leaguePoints'] - prev['leaguePoints']
                        if change > 0:
                            msg = f'{key} just gained {change}lp'
                        else:
                            msg = f'{key} just lost {abs(change)}lp'

                    if rankChange:
                        if change > 0:
                            msg = f'{key} just promotted to {cur["tier"]} {cur["rank"]}'
                        else:
                            msg = f'{key} just demoted to {cur["tier"]} {cur["rank"]}'

                    
                    if key == 'DARKCHERIZARD':
                        if change > 0:
                            msg += f'\n{self.get_winsult()}'
                        else:
                            msg += f'\n{self.get_losesult()}'

                    print(msg)
                    botMsg = discord.Embed(description=f"""{mode}\n{msg}""", color=0x445fa5)
                    await self.channel.send(embed=botMsg)
            except Exception as e:
                print(key, e)


    def get_winsult(self):
        insults = [
            "Always remember to get some fresh air!",
            "How many ranked points will it take to get some bitches?",
            "Nice one, NOT!",
            "Keep it up!",
            "Rankbot is very proud of you ;)."
        ]
        
        return choice(insults)
    
    def get_losesult(self):
        insults = [
            "Better luck next time buddy.",
            "Oof.",
            "99 percent of gamblers quit before they win big. Play again!",
            "Can't end on a loss!",
            "Keep it up!"
        ]
        
        return choice(insults)



  