from modules import client_docteur, client_patient, echanges_donnees
from modules.IHM.IHM_en_Python import launcher, fonctions
import socket
import time

host, port = ('localhost',5566)
FORMAT = 'utf-8'

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port))
print('Connecté au serveur...')

reponse = echanges_donnees.reception(socket)
if reponse == '01gINITCHOIX':
    #Afficher l'interface Qt de choix
    launcher.sequence('Ig',[0,0])
    choix_client = fonctions.Ametier() #'XXp' ou 'XXd'

    if choix_client == 'XXp':
        echanges_donnees.envoi(socket,choix_client)
        client_patient.client_patient(socket)

    elif choix_client == 'XXd':
        echanges_donnees.envoi(socket,choix_client)
        client_docteur.client_docteur(socket)
    else:
        raise NotImplementedError
else:
    raise NotImplemented