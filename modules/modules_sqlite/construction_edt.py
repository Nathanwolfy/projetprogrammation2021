import sqlite3
from . import lire_sql as lsql
from . import rdv_dispo_pris


def nom_jour(jour, mois, annee):
    '''Renvoie le nom du jour grâce à la base de données calendrier'''
    con_1 = lsql.connection_bdd_calendrier()
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nb_jour=? AND mois_jour=? AND annee=?', (jour, mois, annee))
    req = cursor_1.fetchone()
    con_1.close()
    return req[1]

def construction_edt(nom_medecin, jour, mois, annee, heure, minute, motif, note, mail_patient):
    '''Insert dans edt le rendez-vous pris'''
    identifiant_medecin = rdv_dispo_pris.profil_medecin_complet(nom_medecin)[0] #prend l'adresse mail du médecin
    con = lsql.connection_bdd()
    cursor = con.cursor()
    nom_du_jour = nom_jour(jour, mois, annee)
    cursor.execute('SELECT * FROM rdv_dispos WHERE medecin=? AND jour=? AND mois=? AND annee=? AND heure=? AND minute=?', (identifiant_medecin, jour, mois, annee, heure, minute))
    dispo = cursor.fetchone()[6]
    if dispo == 1: #Si le créneau est disponible
        cursor.execute('SELECT * FROM rdvs WHERE motif=?', [motif])
        duree = cursor.fetchone()[2] #edt inclut la durée du rdv
        cursor.execute('INSERT INTO edt VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (identifiant_medecin, nom_du_jour, jour, mois, annee, heure, minute, motif, duree, note, mail_patient))
        con.commit()
    con.close()
    print('Le rendez-vous a été ajouté.') 
