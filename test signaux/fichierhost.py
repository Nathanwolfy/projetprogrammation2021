import socket

host, port = ('localhost',5566)

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((host, port))
socket.listen()
print('Host en ligne...')

#Le script attend une connexion - partie à mettre dans un thread
client, ip = socket.accept()
print(f"Le client d'ip : {ip} s'est connecté.")

while True:
    requete_client = client.recv(1024)
    requete_client = requete_client.decode('utf8')
    print(requete_client)

    if not requete_client: #On ferme si on reçoit une réponse vide
        print('Connexion au client perdue')
        break

    reponse_serveur = input('Données à envoyer :')
    reponse_serveur = reponse_serveur.encode('utf8')
    client.sendall(reponse_serveur)

client.close()
socket.close()
