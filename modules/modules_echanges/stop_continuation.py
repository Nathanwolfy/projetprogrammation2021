from . import echanges_donnees

def arret_processus(socket,erreur):
    """ (socket)
    Fonction qui envoie au thread du serveur disctant l'ordre de stopper puis stop le processus courant.
    """
    requete_fermeture = 'XXgKILLTHREAD'
    echanges_donnees.envoi(socket,requete_fermeture)
    raise erreur