from modules.modules_sqlite import rdv_dispo_pris

a = rdv_dispo_pris.medecins_disponibilites_avec_localisation('generaliste', 'certificat medical', 'TOULOUSE', '27', '01', '2022')
print(a)