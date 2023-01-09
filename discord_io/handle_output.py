from events import *
def execute_output(event):
    if isinstance(event, AddLolAcc):
        print(event.discUser, event.lolName)