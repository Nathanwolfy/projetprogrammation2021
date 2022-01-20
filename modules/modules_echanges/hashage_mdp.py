import hashlib

def hash_mdp(motdepasse):
    """ (str) -> (str)
    Fonction qui renvoie le hachage d'une string rentrée en paramètre.
    """
    hash_mdp = hashlib.sha256(motdepasse.encode("utf-8"))
    return hash_mdp.hexdigest()