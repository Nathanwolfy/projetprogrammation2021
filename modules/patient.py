import time
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions
from . import fonctions_transfert

FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas de mal saisi au départ
    print("Lancement de l'interface de connexion patient ...")
    while clef_valide == 'False':
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '02pINITCONN':
            
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

    confirmation_serveur = socket.recv(32)
    confirmation_serveur = confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '03pINITPRISERDV':
        str_dico_type_rdv = socket.recv(1024).decode(FORMAT)
        dico_type_rdv = fonctions_transfert.FONCTIONACREER(str_dico_type_rdv) #TODO fonction à créer pour convertir un string de dico en dico

        launcher.sequence('IIIp',dico_type_rdv)
        localisation = fonctions.Clocation().encode(FORMAT)
        type_docteur = fonctions.Cpraticien().encode(FORMAT)
        type_rdv = fonctions.CRdV().encode(FORMAT)

        envoi_donnees_prise_rdv = '03pSENDDATARDV'.encode(FORMAT)
        socket.sendall(envoi_donnees_prise_rdv)

        socket.sendall(localisation)
        socket.sendall(type_docteur)
        socket.sendall(type_rdv)
    else:
        raise NotImplementedError

