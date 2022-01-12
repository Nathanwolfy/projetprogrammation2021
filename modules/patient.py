import time
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions

FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):

    confirmation_serveur = socket.recv(32)
    confirmation_serveur = confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '02pINITCONN':
        print("Lancement de l'interface de connexion patient ...")
        launcher.sequence('IIg',[0,0])
        #TODO Proposer la création d'un identifiant de connexion

        clef_patient = fonctions.Bidentifiant() + " " + fonctions.Bmotdepass() #On récupère identifiants et mot de passe rentré par le client
        clef_patient = clef_patient.encode(FORMAT)

        envoi_clef_connexion = '02pSENDCLEF'.encode(FORMAT)
        socket.sendall(envoi_clef_connexion)
        socket.sendall(clef_patient)

    else:
        raise NotImplementedError