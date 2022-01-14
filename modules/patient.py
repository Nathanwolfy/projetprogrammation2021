import time
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions
from . import fonctions_transfert
#TODO Bien gérer les fermetures de fenêtres

FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant mal saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '02pINITCONN':
            launcher.sequence('IIg',identifiant)
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient.encode(FORMAT)

                envoi_clef_connexion = '02pSENDCLEF'.encode(FORMAT)
                socket.sendall(envoi_clef_connexion)
                socket.sendall(clef_patient)

                retour = socket.recv(32)
                clef_valide = retour.decode(FORMAT)

            else: #Le client choisit de créer un compte
                launcher.sequence('Yp',[0,0])
                envoi_donnees_inscription_debut = 'YYpINITSENDDATA'.encode(FORMAT)
                nom_patient = fonctions.Inom().encode(FORMAT)
                prenom_patient = fonctions.Iprenom().encode(FORMAT)
                jour_naiss_patient,mois_naiss_patient,annee_naiss_patient = fonctions.Ijour(),fonctions.Imois(),fonctions.Iannee()
                date_naissance_patient = jour_naiss_patient + "/" + mois_naiss_patient + "/" + annee_naiss_patient
                date_naissance_patient = date_naissance_patient.encode(FORMAT)
                numero_patient = fonctions.Inumero().encode(FORMAT)
                identifiant = fonctions.Bidentifiant().encode(FORMAT)
                motdepasse = fonctions.Bmotdepass().encode(FORMAT)
                envoi_donnees_inscription_fin = 'YYpTERMSENDDATA'.encode(FORMAT)

                socket.sendall(envoi_donnees_inscription_debut)
                socket.sendall(nom_patient)
                socket.sendall(prenom_patient)
                socket.sendall(date_naissance_patient)
                socket.sendall(numero_patient)
                socket.sendall(identifiant)
                socket.sendall(motdepasse)
                socket.sendall(envoi_donnees_inscription_fin)
                clef_valide = 'True'
                
        else:
            raise NotImplementedError

    confirmation_serveur = socket.recv(32)
    confirmation_serveur = confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '03pINITPRISERDV':
        str_dico_type_rdv = socket.recv(1024).decode(FORMAT)
        dico_type_rdv = fonctions_transfert.from_string_to_dict(str_dico_type_rdv)

        launcher.sequence('IIIp',dico_type_rdv)
        localisation = fonctions.Clocation().encode(FORMAT)
        type_docteur = fonctions.Cpraticien().encode(FORMAT)
        type_rdv = fonctions.CRdV().encode(FORMAT)
        date_rdv = fonctions.Cjour() + "/" + fonctions.Cmois() + "/" + fonctions.Cannee()
        date_rdv = date_rdv.encode(FORMAT)

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
        str_dico_disponibilités = socket.recv(256).decode(FORMAT)
        print(str_dico_disponibilités) #On récupère la liste des docteurs dispos et leurs disponibilités
        dico_disponibilités = fonctions_transfert.from_string_to_dict(str_dico_disponibilités)
        print(dico_disponibilités)

        launcher.sequence('IVp',(dico_disponibilités))