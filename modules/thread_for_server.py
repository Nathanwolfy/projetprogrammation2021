from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

#TODO Trouver comment envoyer tout type de données.
#TODO On pourra imaginer un client patient/docteur unique à l'avenir

import threading

FORMAT = 'utf-8'

# Création de la classe pour les threads

class ThreadForServer(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def initialisation_choix_client(self): #On lance la requête pour connaître le choix du client souhaité
        code_initialisation_choix_client = '01gINITCHOIX'.encode(FORMAT) 
        self.conn.sendall(code_initialisation_choix_client)

    def run(self): #Actions à faire au démarrage du Thread
        self.initialisation_choix_client() #On initialise la demande de choix du client
        choix_client = self.conn.recv(8)
        choix_client = choix_client.decode(FORMAT)
        print(choix_client)

        #On lance l'initialisation de l'interface en fonction du choix de client et on déroule les étapes
        if choix_client == 'XXp':
            code_initialisation_connexion_patient = '02pINITCONN'.encode(FORMAT) 
            self.conn.sendall(code_initialisation_connexion_patient)

            #On réceptionne le signal d'envoi des clés de connexion
            #envoi_cles_connexion = self.conn.recv(32)
            #envoi_cles_connexion = envoi_cles_connexion.decode(FORMAT)
            #Faire un test si le client appui sur retour


        elif choix_client == 'XXd':
            code_initialisation_connexion_docteur = '02dINITCONN'.encode(FORMAT)
            self.conn.sendall(code_initialisation_connexion_docteur)
        else:
            pass
            #raise NotImplementedError ?