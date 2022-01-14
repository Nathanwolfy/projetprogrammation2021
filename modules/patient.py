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
            creationcompte_patient = fonctions.Bcreationcompte()
            
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentré par le client
                clef_patient = clef_patient.encode(FORMAT)

                envoi_clef_connexion = '02pSENDCLEF'.encode(FORMAT)
                socket.sendall(envoi_clef_connexion)
                socket.sendall(clef_patient)

                retour = socket.recv(32)
                clef_valide = retour.decode(FORMAT)

            else: #Le client choisit de créer un compte
                pass
                clef_valide = 'True'

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
        date_rdv = fonctions.CdateRdv.encode(FORMAT)

        envoi_donnees_prise_rdv = '03pSENDDATARDV'.encode(FORMAT)
        socket.sendall(envoi_donnees_prise_rdv)

        socket.sendall(localisation)
        socket.sendall(type_docteur)
        socket.sendall(type_rdv)
        socket.sendall(date_rdv)
    else:
        raise NotImplementedError

    confirmation_serveur = socket.recv(32)
    confirmation_serveur = confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '04pINITAFFDISPO':
        str_liste_docteurs_dispos = socket.recv(128).decode(FORMAT) #On récupère la liste des docteurs dispos et leurs disponibilités
        str_liste_disponibilités = socket.recv(256).decode(FORMAT)
        liste_docteurs_dispos = fonctions_transfert.FONCTIONACREER(str_liste_docteurs_dispos)
        liste_disponibilités = fonctions_transfert.FONCTIONACREER(str_liste_disponibilités)

        launcher.sequence('IVp',(liste_docteurs_dispos,liste_disponibilités))