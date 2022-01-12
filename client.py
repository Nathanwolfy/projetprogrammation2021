from modules import patient
from modules import docteur
from modules.IHM.IHM_en_Python import launcher
from modules.IHM.IHM_en_Python import fonctions
import socket
import time

host, port = ('localhost',5566)
FORMAT = 'utf-8'

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port))
print('Connecté au serveur...')

while True: #Attente pour l'initialisation
    reponse = socket.recv(32)
    reponse = reponse.decode(FORMAT)
    if reponse == '01gINITCHOIX':
        break
    time.sleep(0.1)

#Afficher l'interface Qt de choix
launcher.sequence('Ig',[0,0])
choix_client = fonctions.Ametier() #'XXp' ou 'XXd'
choix_client_encode = choix_client.encode(FORMAT)

if choix_client == 'XXp':
    
    socket.sendall(choix_client_encode)
    patient.client_patient(socket)

    confirmation_serveur = socket.recv(32)
    confirmation_serveur = confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '02pINITCONN':
        print("Lancement de l'interface de connexion patient ...")
        launcher.sequence('IIg',[0,0])
        #TODO Proposer la création d'un identifiant de connexion
        print('a')
        dentifiant_patient = fonctions.Bidentifiant()
        motdepasse_patient = fonctions.Bmotdepass()

elif choix_client == 'XXd':
    socket.sendall(choix_client_encode)
    docteur.client_docteur(socket)
else:
    raise NotImplementedError

time.sleep(2)