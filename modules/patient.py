#Import
FORMAT = 'utf-8'

def client_patient(socket):
    message = '\nhi'.encode(FORMAT)
    socket.sendall(message)