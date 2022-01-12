import time
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions

FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas de mal saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '02pINITCONN':
            print("Lancement de l'interface de connexion patient ...")
            launcher.sequence('IIg',identifiant)
            #TODO Proposer la création d'un identifiant de connexion
            identifiant = fonctions.Bidentifiant()
            motdepasse = fonctions.Bmotdepass()
            clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentré par le client
            clef_patient = clef_patient.encode(FORMAT)

            envoi_clef_connexion = '02pSENDCLEF'.encode(FORMAT)
            socket.sendall(envoi_clef_connexion)
            socket.sendall(clef_patient)

            retour = socket.recv(32)
            clef_valide = retour.decode(FORMAT)
        else:
            raise NotImplementedError
