from app.account import Account
from app.client import Client

from decimal import *


class TestClient:
    def test_init_client(self):
        # Given
        name = "John Doe"
        # When
        client = Client(name)
        # Then
        assert client.name == name

    def test_client_default_account(self):
        # Given
        name = "John Doe"
        # When
        client = Client(name)
        # Then
        assert client.account is not None
        assert isinstance(client.account, Account)

    def test_client_with_account(self):
        # Given
        name = "John Doe"
        account = Account(Decimal(10))
        # When
        client = Client(name, account)
        # Then
        assert client.account is account
