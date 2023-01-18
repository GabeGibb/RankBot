
from api_info.valQ import get_val_info
class ValAcct:
    def __init__(self, username, tagline):
        self.name = username
        self.tag = tagline
        self.info = {}
        self.prevInfo = {}
        self.set_info()

    def set_info(self):
        self.prevInfo = self.info
        self.info = get_val_info(self.name, self.tag)

    
    