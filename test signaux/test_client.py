#coding:utf-8
import socket

host, port = ('localhost',5566) #ou 127.0.0.1

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host,port))
    print('client connected')

    data = 'aebazgeoiazeayeaééé'
    data = data.encode("utf8") #data codée en utf-8 pour éviter les problèmes avce les accents
    socket.sendall(data) #méthode send ou sendall

except ConnectionRefusedError: 
    print('connexion to server failed')

finally:
    socket.close()