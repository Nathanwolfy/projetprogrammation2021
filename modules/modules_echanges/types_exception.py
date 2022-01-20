class ClientDisconnectedError(Exception):
    """Exception en cas de déconnexion du client distant."""
    def __init__(self):
        super().__init__("Le client distant s'est déconnecté.")

class InvalidClientReponseError(Exception):
    """Exception en cas de réponse invalide du client distant."""
    def __init__(self):
        super().__init__("Le client distant a fourni une réponse non valide.")

class InvalidServerReponseError(Exception):
    """Exception en cas de réponse invalide du serveur distant."""
    def __init__(self):
        super().__init__("Le serveur distant a fourni une réponse non valide.")

class InvalidUserInputError(Exception):
    """Exception en cas d'entrée invalide de la part de l'utilisateur."""
    def __init__(self):
        super().__init__("L'utilisateur a fourni une entrée invalide.")
