import threading

# Création de la classe pour les threads

class ThreadForClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        pass  
        #Actions à faire une fois le thread lancé
        #Trouver comment discriminer patient et docteur et les identifier
        #Trouver quelles actions à faire dans quels cas
        #Trouver un moyen de revenir en arrière et de modifier les données si besoin
