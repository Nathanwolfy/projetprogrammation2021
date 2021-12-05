#coding:utf-8
import socket

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket avec constante
socket.bind((host, port)) #on associe le socket à l'adresse et au port

print('server is booted')

while True:
    socket.listen() #on met en écoute le port, 10=valeur du nombre de tentatives
    conn, address = socket.accept() #on accepte les connexions
    print('server is listening')

    data = conn.recv(1024) #réception et taille de buffer = 256,1024,2048..
    data = data.decode('utf8') #on décode la data
    print(data)
conn.close() #on ferme la connexion
socket.close() #on ferme le socket