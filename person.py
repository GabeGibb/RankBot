
import lolQ

class Person:

    def __init__(self):
        self.lolAcccounts = {}
        self.valAccounts = {}

    def add_lol_acc(self):
        id = lolQ.find_lol_id('kelluu')
        lolQ.get_rank_info(id)