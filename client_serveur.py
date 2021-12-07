import socket
from modules.thread_for_client import ThreadForClient

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création du socket
socket.bind((host, port)) #On associe le socket à l'adresse et au port
print('Server is booted')

while True:
    socket.listen() #On met en écoute le port, valeur du nombre de tentatives facltutatif
    conn, address = socket.accept() #On accepte les connexions
    print(f'client : {conn} is connected')

    threadclient = ThreadForClient(conn) #Création d'un thread par nouvelle connexion
    threadclient.start()

conn.close() #On ferme la connexion
socket.close() #On ferme le socket
