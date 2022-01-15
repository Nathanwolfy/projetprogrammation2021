import socket
from modules.thread_for_server import ThreadForServer


host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création du socket
socket.bind((host, port)) #On associe le socket à l'adresse et au port
print('Le serveur est lancé.')

while True:
    socket.listen() #On met en écoute le port, valeur du nombre de tentatives facltutatif
    conn, address = socket.accept() #On accepte les connexions
    print(f'Le client : {conn} est connecté.')

    threadclient = ThreadForServer(conn) #Création d'un thread par nouvelle connexion
    threadclient.start()

conn.close() #On ferme la connexion

socket.close() #On ferme le socket