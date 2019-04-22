from app.account import Account


class Client:
    def __init__(self, name: str, account: Account = Account()) -> None:
        self.name = name
        self.account = account
