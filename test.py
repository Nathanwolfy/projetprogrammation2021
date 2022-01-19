from modules.modules_echanges import hashage_mdp

motdepasse = 'ceciestunsupermotdepasse'
print(hashage_mdp.hash_mdp(motdepasse))