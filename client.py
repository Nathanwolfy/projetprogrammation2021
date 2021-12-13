import modules.patient as patient
import modules.docteur as docteur
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
choix_client = 'XXp' # ou 'XXd' # #Récupérer le choix_client à l'aide de l'interface Qt
choix_client_encode = choix_client.encode(FORMAT)

if choix_client == 'XXp':
    message = input()
    socket.sendall(choix_client_encode)
    patient.client_patient(socket)
elif choix_client == 'XXd':
    socket.sendall(choix_client_encode)
    docteur.client_docteur(socket)
else:
    pass #Erreur ?

time.sleep(10)