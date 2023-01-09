
from api_info.lolQ import *


class Person:

    def __init__(self):
        self.lolIDs = {}
        self.lolInfo = {}
        self.valAccounts = {}

    def add_lol_acc(self, user):
        id = find_lol_id(user)
        self.lolIDs[user] = id
        self.set_lol_info(user)
     

    def set_lol_info(self, user):
        id = self.lolIDs[user]
        self.lolInfo[id] = get_lol_info(id)
        print(self.lolInfo)

        
