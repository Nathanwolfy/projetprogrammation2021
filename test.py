"""
from modules.modules_IHM.IHM_en_Python import launcher
a = {'Dr siphano lebeau': ['8:00', '8:15', '8:30', '8:45', '9:00', '9:15', '9:30', '9:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30']}

launcher.sequence('IVp',a)"""

from modules.modules_sqlite import rdv_dispo_pris, exploitation_sql_patient
from modules.modules_echanges import conversion_types
from modules.modules_IHM.IHM_en_Python import launcher

#a = rdv_dispo_pris.medecins_disponibilites_avec_localisation('generaliste','certificat medical', 'TOULOUSE', '27', '01','2022')
#b = fonctions_transfert.from_string_to_dict(str(a))
#print(b)
#launcher.sequence('IVp',(b))
#c = fonctions_transfert.from_string_to_dict('{}')
#print(c)
#exploitation_sql_patient.inscription_patient('Karim','Aziz','01','01','2000','karim.aziz@gmail.com','0751515151','1234','1234')