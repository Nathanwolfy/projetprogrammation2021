#coding:utf-8
import socket
import threading

class ThreadForClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)
        self.conn.send('hi from server'.encode('utf8'))

#----------------

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création du socket
socket.bind((host, port)) #On associe le socket à l'adresse et au port

print('server is booted')

while True:
    socket.listen() #on met en écoute le port, 10=valeur du nombre de tentatives
    conn, address = socket.accept() #on accepte les connexions
    print(f'client : {conn},{address} is connected')

    threadclient = ThreadForClient(conn)
    threadclient.start()

conn.close() #on ferme la connexion
socket.close() #on ferme le socket
