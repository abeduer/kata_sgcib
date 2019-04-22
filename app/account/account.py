from decimal import *


class Account:
    def __init__(self, balance: Decimal = Decimal(0)) -> None:
        self.balance = balance

    def withdraw(self, amount: Decimal) -> None:
        self.balance = self.balance - amount
