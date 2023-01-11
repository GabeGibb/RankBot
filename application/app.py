from application.lolAcct import LolAcct
from application.events import *


class App:
    def __init__(self):
        self.lolAccts = {}

    def add_lol_acct(self, userName):  
        self.lolAccts[userName] = LolAcct(userName)
        # return AccAdded(self.lolAccts[userName])

    def get_lol_acct(self, userName):
        return ShowAcc(self.lolAccts[userName])
        
    def get_lol_accts(self):
        return ShowAccs(self.lolAccts)





