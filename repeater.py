
from discord.ext import commands, tasks

from application.events import *


class Repeater(commands.Cog):
    def __init__(self, bot, app):
        self.bot = bot
        self.app = app
        self.channel = None


    @tasks.loop(seconds=60.0)
    async def get_data(self):
        
        lolDict = {'IRON': 0, 'BRONZE': 1, 'SILVER': 2, 'GOLD': 3, 'PLATINUM': 4, 'DIAMOND': 5, 'MASTER': 6, 'GRANDMASTER': 7, 'CHALLENGER': 8}
        numDict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
        num = 0

        #Silver II 36lp
        for key, value in self.app.lolAccts.items():
            value.set_info()
            
            for p, c in zip(value.prevInfo.items(), value.info.items()):
                mode = c[0]
                prev = p[1]
                cur = c[1]
                if prev['wins'] == cur['wins'] or prev['losses'] == cur['wins']:
                    continue

                msg = ''
                rankChange = False
                if prev['tier'] == cur['tier']:
                    if prev['rank'] == cur['rank']:
                        if prev['leaguePoints'] == cur['leaguePoints']:
                            continue
                        else:
                            change = cur['leaguePoints'] - prev['leaguePoints']
                            if change > 0:
                                msg = f'Congrats {key}! You just gained {change} lp'
                            else:
                                msg = f'Unlucky {key}! You just lost {abs(change)} lp. Better luck next time!'
                    else:
                        change = numDict[cur['rank']] - numDict[prev['rank']]
                        rankChange = True
                else:
                    pRank = lolDict[prev['tier']]
                    cRank = lolDict[cur['tier']]
                    change = cRank - pRank
                    rankChange = True
                if rankChange:
                    if change > 0:
                        msg = f'Congrats {key}! You just got promotted to {cur["tier"]} {cur["rank"]}'
                    else:
                        msg = f'Unlucky {key}! You just got demoted to {cur["tier"]} {cur["rank"]}'
                
                await self.channel.send(f'{mode}\n{msg} {num}')



    



  