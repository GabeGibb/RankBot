from api_info.lolQ import *

class LolAcct:

    def __init__(self, name):
        self.id = None
        self.name = name
        self.info = {}

        self.add_acct()
        self.startInfo = self.info
        self.prevInfo = self.info

    def add_acct(self):
        self.id = find_lol_id(self.name)
        self.set_info()
     
    def set_info(self):
        self.prevInfo = self.info
        self.info = get_lol_info(self.id)

    def set_end_of_day(self):
        self.set_info()
        self.startInfo = self.info
    
    def prev_elo_change(self):
        return self.info['leaguePoints'] - self.prevInfo['leaguePoints']

    def last_elo_change(self):
        return self.info['leaguePoints'] - self.startInfo['leaguePoints']
    



        
