from app.bank import Bank


class TestBank:
    def test_new_bank(self):
        # Given
        bank_name = "Société Générale"
        # When
        new_bank = Bank(bank_name)
        # Then
        assert new_bank.name == bank_name

    def test_new_bank_client_list_is_empty(self):
        # Given
        bank_name = "Société Générale"
        # When
        new_bank = Bank(bank_name)
        # Then
        assert new_bank.client_list == []
