FORMAT = 'utf-8'
import time

def exposant_p2_sup(nbr):
    """(int) -> (str)
    Fonction qui pour un nombre donné renvoie l'exposant de la puissance de deux supérieure au nombre codé sur deux chiffres sous forme d'un string."""
    n = 0
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
    return message if message != 'NULL' else ''

def envoi(support,message):
    """(support,str)
    Fonction qui pour un support (socket : côté client, connexion : côté serveur) et message donnés envoie le successivement l'exposant de la puissance de 2 supérieure à la taille du message ainsi que le message."""
    message = message.encode(FORMAT) if message != '' else 'NULL'.encode(FORMAT)
    nbr = exposant_p2_sup(len(message)).encode(FORMAT)
    support.sendall(nbr)
    time.sleep(0.001)
    support.sendall(message)
    time.sleep(0.001)

def check_donnes_non_vides(donnees):
    """(tuple) -> (Bool)
    Fonction qui pour un tuple donné renvoie False si l'une de ses composantes est une string vide et True sinon.
    """
    flag = True
    for k in range(len(donnees)):
        if donnees[k] == '':
            flag = False
            return flag
        else:
            pass
    return flag
