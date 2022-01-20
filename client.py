from modules import client_docteur, client_patient
from modules.modules_IHM.IHM_en_Python import launcher
from modules.modules_echanges import echanges_donnees,types_exception,stop_continuation
import socket

host, port = ('localhost',5566) #On choisit comme adresse celle locale et un port non affecté

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port)) #Connexion du socket au l'adresse et le port
print('Connecté au serveur...')

reponse = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la fenêtre de choix du client
if reponse == '01gINITCHOIX': #Validation du lancement de la fenêtre de choix du client par le serveur
    #Afficher l'interface Qt de choix
    fenetre_choix_client = launcher.Achoixdocuser_herit()
    launcher.exec_fenetre(fenetre_choix_client)
    continuation = fenetre_choix_client.continuation
    choix_client = fenetre_choix_client.choix_client #'XXp' ou 'XXd'

    if choix_client == 'XXp': #Le client patient est choisi
        echanges_donnees.envoi(socket,choix_client) #On informe le serveur du choix du client patient
        client_patient.client_patient(socket) #On démarre le client patient

    elif choix_client == 'XXd': #Le client docteur est choisi
        echanges_donnees.envoi(socket,choix_client) #On informe le serveur du choix du client docteur
        client_docteur.client_docteur(socket) #On démarre le client docteur

    elif not continuation: #Si le client ne clique sur aucun bouton donc ferme la fenêtre, on envoie au serveur l'indication et on termine le script client
        stop_continuation.arret_processus(socket)

    else: #Dans tous les autres cas, c'est un erreur
        raise types_exception.InvalidServerReponseError

else: #Si le serveur ne valide pas, l'application s'arrête
    raise types_exception.InvalidServerReponseError