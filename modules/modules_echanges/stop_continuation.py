import sys
from . import echanges_donnees

def arret_processus(socket):
    """Fonction qui envoie au thread l'ordre de stopper puis stop le processus.
    """
    requete_fermeture = 'XXgKILLTHREAD'
    echanges_donnees.envoi(socket,requete_fermeture)
    sys.exit()