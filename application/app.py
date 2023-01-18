from application.lolAcct import LolAcct
from application.valAcct import ValAcct
from application.events import *


class App:
    def __init__(self):
        self.lolAccts = {}
        self.valAccts = {}

    def add_lol_acct(self, username):  
        try:
            self.lolAccts[username] = LolAcct(username)
        except:
            pass

    def add_val_acct(self, username, tagline):
        try:
            self.valAccts[username] = ValAcct(username, tagline)
        except:
            pass
        


    # def get_lol_acct(self, userName):
    #     return ShowAcc(self.lolAccts[userName])
        
    # def get_lol_accts(self):
    #     return ShowAccs(self.lolAccts)





