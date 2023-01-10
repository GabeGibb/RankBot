from api_info.lolQ import *

class LolAcct:

    def __init__(self, name):
        self.id = None
        self.name = name
        self.info = {}
        self.add_acct()

    def add_acct(self):
        self.id = find_lol_id(self.name)
        self.set_info()
     

    def set_info(self):
        self.info = get_lol_info(self.id)

    



        
