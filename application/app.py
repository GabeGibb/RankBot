from application.lolAcct import LolAcct
from application.valAcct import ValAcct


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
        




