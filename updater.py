
import discord
from discord.ext import commands, tasks
from asyncio import sleep


class Updater(commands.Cog):
    def __init__(self, bot, app):
        self.bot = bot
        self.app = app
        self.channel = None

    @tasks.loop(seconds=60.0)
    async def val_update(self):
        for key, value in self.app.valAccts.items():
            sleep(0)
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

            botMsg = discord.Embed(description=f"""VALORANT RANKED\n{msg}""", color=0xfa4454)
            await self.channel.send(embed=botMsg)



    @tasks.loop(seconds=60.0)
    async def lol_update(self):
        lolDict = {'IRON': 0, 'BRONZE': 1, 'SILVER': 2, 'GOLD': 3, 'PLATINUM': 4, 'DIAMOND': 5, 'MASTER': 6, 'GRANDMASTER': 7, 'CHALLENGER': 8}
        numDict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}

        for key, value in self.app.lolAccts.items():
            sleep(0)
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
                    msg += '\nRegardless of the outcome, look at this loser playing League of Legends LOL!'
                print(msg)
                botMsg = discord.Embed(description=f"""{mode}\n{msg}""", color=0x445fa5)
                await self.channel.send(embed=botMsg)



    



  