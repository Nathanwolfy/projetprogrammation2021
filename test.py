from modules.modules_IHM.IHM_en_Python import launcher
from modules.modules_sqlite import lire_sql
import hashlib

FORMAT = 'utf-8'
#a = lire_sql.liste_type_medecin()
#launcher.sequence('Yd',a)

#dico_type_rdv = lire_sql.dictionnaire_pour_qt()
#launcher.sequence('IIIp',(dico_type_rdv,False))
hash_mdp = hashlib.sha1('mdp'.encode(FORMAT))
print(hash_mdp.hexdigest())