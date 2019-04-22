from app.client import Client


class TestClient:
    def test_new_client(self):
        # Given
        client_name = "John Doe"
        # When
        new_client = Client(client_name)
        # Then
        assert new_client.name == client_name

    def test_new_client_id_not_none(self):
        # Given
        client_name = "John Doe"
        # When
        new_client = Client(client_name)
        # Then
        assert new_client.client_id is not None

    def test_new_client_account_list_is_empty(self):
        # Given
        client_name = "John Doe"
        # When
        new_client = Client(client_name)
        # Then
        assert new_client.account_list == []
