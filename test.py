from modules.modules_IHM.IHM_en_Python import launcher
from modules.modules_sqlite import lire_sql


a = lire_sql.liste_type_medecin()
launcher.sequence('Yd',a)
