from app.account import Account


class Client:
    def __init__(self, name, account=Account()):
        self.name = name
        self.account = account
