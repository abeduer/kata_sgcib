from decimal import *

from app.account import Account


class TestAccount:
    def test_new_account(self):
        # Given
        account_owner = "12345"
        # When
        new_account = Account(account_owner)
        # Then
        assert new_account.owner == account_owner

    def test_new_account_id_not_none(self):
        # Given
        account_owner = "12345"
        # When
        new_account = Account(account_owner)
        # Then
        assert new_account.account_id is not None

    def test_new_account_balance_is_empty(self):
        # Given
        account_owner = "12345"
        # When
        new_account = Account(account_owner)
        # Then
        assert new_account.balance == Decimal(0)
