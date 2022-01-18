FORMAT = 'utf-8'

def exposant_p2_sup(nbr):
    """(int) -> (str)
    Fonction qui pour un nombre donné renvoie l'exposant de la puissance de deux supérieure au nombre codé sur deux chiffres sous forme d'un string."""
    n = 1
    while nbr > 2**n:
        n+=1
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)

def reception(support):
    """(support) -> (str)
    Fonction qui pour un support (socket : côté client, connexion : côté serveur) donné renvoie le message reçu."""
    taille_mess_exposant = support.recv(2).decode(FORMAT)
    message = support.recv(2**int(taille_mess_exposant)).decode(FORMAT)
    print(message)
    return message if message != 'NULL' else ''

def envoi(support,message):
    """(socket,str)
    Fonction qui pour un support (socket : côté client, connexion : côté serveur) et message donnés envoie le successivement l'exposant de la puissance de 2 supérieure à la taille du message ainsi que le message."""
    message = message.encode(FORMAT) if message != '' else 'NULL'.encode(FORMAT)
    nbr = exposant_p2_sup(len(message)).encode(FORMAT)
    print(message)
    support.sendall(nbr)
    support.sendall(message)