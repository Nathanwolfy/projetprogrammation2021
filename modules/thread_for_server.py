from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

#TODO Trouver comment envoyer tout type de données.
#TODO On pourra imaginer un client patient/docteur unique à l'avenir

import threading
from .modules_sqlite import exploitation_sql_patient

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

        #On lance l'initialisation de l'interface en fonction du choix de client et on déroule les étapes
        if choix_client == 'XXp':
            clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas.
            while clef_valide == 'False':
                code_initialisation_connexion_patient = '02pINITCONN'.encode(FORMAT) 
                self.conn.sendall(code_initialisation_connexion_patient)

                #On réceptionne le signal d'envoi des clés de connexion
                reponse = self.conn.recv(32)
                reponse = reponse.decode(FORMAT)
                clef_valide = False

                if reponse == '02pSENDCLEF':
                    clef_connexion = self.conn.recv(64)
                    clef_connexion = clef_connexion.decode(FORMAT).split(" ")
                    identifiant_patient, motdepasse_patient = clef_connexion[0], clef_connexion[1]
                    
                    clef_valide = str(exploitation_sql_patient.connexion_patient_reussie(identifiant_patient,motdepasse_patient)) #On vérifie que la clef de connexion est valide

                    validation = clef_valide.encode(FORMAT)
                    self.conn.sendall(validation)
                else:
                    raise NotImplementedError

            #On initie la suite



        elif choix_client == 'XXd':
            code_initialisation_connexion_docteur = '02dINITCONN'.encode(FORMAT)
            self.conn.sendall(code_initialisation_connexion_docteur)
        else:
            pass
            #raise NotImplementedError ?