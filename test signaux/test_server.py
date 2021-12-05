import socket

host, port = ('',5566)

socket = socket.socket(socket.AF_INT, socket.SOCK_STREAM) #création du socket avec constante
socket.bind((host, port)) #on associe le socket à l'adresse et au port

print('server is booted')

while True:
    socket.listen(10) #on met en écoute le port, 10=valeur du nombre de tentatives
    conn, address = socket.accept() #on accepte les connexions
    print('server is listening')

conn.close() #on ferme la connexion
socket.close() #on ferme le socket