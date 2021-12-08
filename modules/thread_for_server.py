from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

import threading

FORMAT = 'utf-8'

# Création de la classe pour les threads

class ThreadForServer(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def initialisation_choix_client(self): #On lance la requête pour connaître le choix du client souhaité
        code_initialisation_choix_client = '01gINITCHOIX'.encode(FORMAT) 
        self.conn.send(code_initialisation_choix_client)

    def run(self): #Actions à faire au démarrage du Thread
        self.initialisation_choix_client() #On initialise la demande de choix du client
        choix_client = self.conn.recv(8)

        if choix_client == 'docteur':
            pass
        elif choix_client == 'patient':
            pass
        else:
            raise NotImplementedError