import socket

host, port = ('localhost',5566)

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host,port))
print('Client en ligne...')

while True:
    requete_client = input('Requête à envoyer :')
    requete_client = requete_client.encode('utf8')

    socket.send(requete_client)

    reponse_serveur = socket.recv(1024)
    reponse_serveur = reponse_serveur.decode('utf8')
    print(reponse_serveur)