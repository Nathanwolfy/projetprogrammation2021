import time
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions

FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):

    confirmation_serveur = socket.recv(32)
    confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '02pINITCONN':
        print("Lancement de l'interface de connexion patient ...")
        launcher.sequence('IIg',[0,0])
        #TODO Proposer la création d'un identifiant de connexion
        identifiant_patient = fonctions.Bidentifiant()
        motdepasse_patient = fonctions.Bmotdepass() #Comment encrypter les mots de passe ?

        identifiant_patient = identifiant_patient.encode(FORMAT)
        motdepasse_patient = motdepasse_patient.encode(FORMAT)

        #On signale au serveur que l'on va envoyer les clés de connexion et on envoie successivement l'identifiant et le mot de passe pour vérifier qu'ils sont bien dans la base de données
        envoi_cles_connexion = '02pSENDCONN'.encode(FORMAT)
        socket.sendall(envoi_cles_connexion)
        time.sleep(WAITINGTIME)
        socket.sendall(identifiant_patient)
    else:
        raise NotImplementedError