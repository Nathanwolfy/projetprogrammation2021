from base64 import encode
import sys

from .IHM.IHM_en_Python import launcher
from .IHM.IHM_en_Python import fonctions
from . import fonctions_transfert

FORMAT = 'utf-8'

def client_docteur(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle l'est
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '02dINITCONN':
            launcher.sequence('IIg',identifiant)
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le docteur choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le docteur
                clef_patient = clef_patient.encode(FORMAT)

                envoi_clef_connexion = '02dSENDCLEF'.encode(FORMAT)
                socket.sendall(envoi_clef_connexion)
                socket.sendall(clef_patient)

                retour = socket.recv(32)
                clef_valide = retour.decode(FORMAT)

            else: #Le docteur choisit de créer un compte
                launcher.sequence('Yd',[0,0])
                envoi_donnees_inscription_debut = 'YYdINITSENDDATA'.encode(FORMAT)
                nom_docteur = .encode(FORMAT)
                prenom_docteur = .encode(FORMAT)
                ville_de_pratique = .encode(FORMAT)
                adresse_docteur = .encode(FORMAT)
                code_postal_docteur = .encode(FORMAT)
                numero_docteur = .encode(FORMAT)
                identifiant = .encode(FORMAT)
                motdepasse = .encode(FORMAT)
                envoi_donnees_inscription_fin = 'YYdTERMSENDDATA'.encode(FORMAT)

                socket.sendall(envoi_donnees_inscription_debut)
                socket.sendall(nom_docteur)
                socket.sendall(prenom_docteur)
                socket.sendall(ville_de_pratique)
                socket.sendall(adresse_docteur)
                socket.sendall(code_postal_docteur)
                socket.sendall(numero_docteur)
                socket.sendall(identifiant)
                socket.sendall(motdepasse)
                socket.sendall(envoi_donnees_inscription_fin)
                clef_valide = 'True' #Le docteur a créé son compte, il est donc bien identifié
                
        else:
            raise NotImplementedError