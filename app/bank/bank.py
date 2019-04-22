class Bank:
    def __init__(self, name):
        self.name = name
        self.client_list = []

    def add_new_client(self, client):
        self.client_list.append(client)
