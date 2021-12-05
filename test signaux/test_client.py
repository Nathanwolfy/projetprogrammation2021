import socket

host, port = ('localhost',5566) #ou 127.0.0.1

socket = socket.socket(socket.AF_INT, socket.SOCK_STREAM)

try:
    socket.connect((host,port))
    print('client connected')
except ConnectionRefusedError: 
    print('connexion to server failed')

finally:
    socket.close()