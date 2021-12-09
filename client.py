import modules.patient as patient
import socket

host, port = ('localhost',5566)
FORMAT = 'utf-8'

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port))
print('Connecté au serveur...')

#TODO système pour attendre la requête pour démarrer l'initialisation du choix

choix_client = 'patient'.encode(FORMAT)
socket.sendall(choix_client)