
from events import *

def get_words(list, start, stop):
    return [c.lower() for c in list[start:stop]]

def decide_command(msg):
    content = msg.content
    cList = content.split()

    if get_words(cList, 0, 2) == ['lol', 'add']:
        return AddLolAcc(cList[2], msg.author)


# def add_lol_acc():




    