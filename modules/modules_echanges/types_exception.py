class ClientDisconnectedError(Exception):
    def __init__(self):
        super().__init__("Le client distant s'est déconnecté.")

class InvalidClientReponseError(Exception):
    def __init__(self):
        super().__init__("Le client distant a fourni une réponse non valide.")

class InvalidServerReponseError(Exception):
    def __init__(self):
        super().__init__("Le serveur distant a fourni une réponse non valide.")
