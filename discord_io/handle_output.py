from application.events import *
import discord

def get_output(event):
    if event is None:
        return ''
    
    elif isinstance(event, Commands):
        msg = 'lol add username\n'\
        'lol show username\n'\
        'lol show'
        return discord.Embed(description=f"""{msg}""", color=0x00ff00)

    elif isinstance(event, AccAdded):
        return f'Ok {event.acct.name} was added.'

        
    elif isinstance(event, ShowAcc):
        msg = ''
        for key, value in event.acct.info.items():
            msg += f'{key}\n'
            msg += f'\t{value["tier"]} {value["rank"]} {value["leaguePoints"]} lp\n'

        return msg

    elif isinstance(event, ShowAccs):
        msg = ''
        for acct in event.accts:
            msg += f'{acct}\n'

        return msg