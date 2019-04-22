import uuid
from app.account import Account


class Client:
    def __init__(self, name):
        self.client_id = uuid.uuid1()
        self.name = name
        self.account_list = []

    def add_new_account(self):
        account = Account(self.client_id)
        self.account_list.append(account)
