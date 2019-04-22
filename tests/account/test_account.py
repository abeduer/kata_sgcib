from decimal import *

from app.account import Account


class TestAccount:
    def test_init_account(self):
        # Given

        # When
        account = Account()
        # Then
        assert account.balance == Decimal(0)

    def test_init_account_with_balance(self):
        # Given
        balance = Decimal(10)
        # When
        account = Account(balance)
        # Then
        assert account.balance == Decimal(10)

    def test_withdraw(self):
        # Given
        account = Account(Decimal(100))
        amount = Decimal(10)
        # When
        account.withdraw(amount)
        # Then
        assert account.balance == Decimal(90)
