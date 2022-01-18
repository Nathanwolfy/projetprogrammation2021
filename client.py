from modules import client_docteur, client_patient
from modules.modules_IHM.IHM_en_Python import launcher, fonctions
import socket
import sys

from modules.modules_echanges import echanges_donnees

host, port = ('localhost',5566) #On choisit comme adresse celle locale et un port non affecté

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port)) #Connexion du socket au l'adresse et le port
print('Connecté au serveur...')

reponse = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la fenêtre de choix du client
if reponse == '01gINITCHOIX': #Validation du lancement de la fenêtre de choix du client par le serveur
    #Afficher l'interface Qt de choix
    launcher.sequence('Ig',[0,0]) #TODO supprimer argument inutile
    continuation = fonctions.continus()
    choix_client = fonctions.Ametier() #'XXp' ou 'XXd'

    if choix_client == 'XXp': #Le client patient est choisi
        echanges_donnees.envoi(socket,choix_client) #On informe le serveur du choix du client patient
        client_patient.client_patient(socket) #On démarre le client patient

    elif choix_client == 'XXd': #Le client docteur est choisi
        echanges_donnees.envoi(socket,choix_client) #On informe le serveur du choix du client docteur
        client_docteur.client_docteur(socket) #On démarre le client docteur

    elif not continuation: #Si le client ne clique sur aucun bouton donc ferme la fenêtre, on envoie au serveur l'indication et on termine le script client
        requete_fermeture = 'XXgKILLTHREAD'
        echanges_donnees.envoi(socket,requete_fermeture)
        sys.exit()

    else: #Dans tous les autres cas, c'est un erreur
        raise NotImplementedError

else: #Si le serveur ne valide pas, l'application s'arrête
    raise NotImplementedError