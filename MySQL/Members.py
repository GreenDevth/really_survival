from db.db_config import MySQL


class Users:
    def __init__(self):
        self.db = MySQL()

class Steam:
    def __init__(self):
        self.db = MySQL()

class Bank:
    def __init__(self):
        self.db = MySQL()