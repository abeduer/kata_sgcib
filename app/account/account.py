import uuid
from decimal import *


class Account:
    def __init__(self, balance=Decimal(0)):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
