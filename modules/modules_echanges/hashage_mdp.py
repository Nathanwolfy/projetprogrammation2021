import hashlib

def hash_mdp(motdepasse):
    hash_mdp = hashlib.sha1(motdepasse.encode("utf-8"))
    return hash_mdp.hexdigest()