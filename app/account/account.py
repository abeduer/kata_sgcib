import uuid
from decimal import *


class Account:
    def __init__(self, owner, balance=Decimal(0)):
        self.account_id = uuid.uuid1()
        self.owner = owner
        self.balance = balance
