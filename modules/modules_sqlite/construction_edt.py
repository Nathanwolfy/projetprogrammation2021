import sqlite3
from . import lire_sql as lsql
from . import rdv_dispo_pris


def nom_jour(jour, mois, annee):
    con_1 = lsql.connection_bdd_calendrier()
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nb_jour=? AND mois_jour=? AND annee=?', (jour, mois, annee))
    req = cursor_1.fetchone()
    con_1.close()
    return req[1]

def construction_edt(nom_medecin, jour, mois, annee, heure, minute, motif, note):
    identifiant_medecin = rdv_dispo_pris.profil_medecin_complet(nom_medecin)[0]
    con = lsql.connection_bdd()
    cursor = con.cursor()
    nom_du_jour = nom_jour(jour, mois, annee)
    cursor.execute('SELECT * FROM rdv_dispos WHERE medecin=? AND jour=? AND mois=? AND annee=? AND heure=? AND minute=?', (identifiant_medecin, jour, mois, annee, heure, minute))
    dispo = cursor.fetchone()[6]
    if dispo == 1:
        cursor.execute('SELECT * FROM rdvs WHERE motif=?', [motif])
        duree = cursor.fetchone()[2]
        cursor.execute('INSERT INTO edt VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (identifiant_medecin, nom_du_jour, jour, mois, annee, heure, minute, motif, duree, note))
        con.commit()
    con.close()
    print('Le rendez-vous a été ajouté.') 
