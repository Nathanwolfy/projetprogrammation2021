import sqlite3
import emploidutemps as e

def connection():
    try:
        connect = sqlite3.connect('donnees.db')
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')


con = connection()
cursor = con.cursor()

def creneau_dispo_motif(motif):
    cursor.execute('SELECT * FROM rdvs')
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == motif:
            duree_rdv = row[2]
            type_medecin = row[0]
    cursor.execute('SELECT travail, mail FROM medecins WHERE travail=?', [type_medecin])
    rows_medecin = cursor.fetchall()
    for row_medecin in rows_medecin:
        dictionnaire_rdv_dispos_par_medecin = {}
        duree = 0
        heure_debut = e.Heure(0, 0)
        liste_heure_dispo  = []
        for heure in range(8, 18):
            for minute in range(0, 46, 15):
                cursor.execute('SELECT * FROM rdv_dispos WHERE heure=? AND minute=? AND medecin=?', (heure, minute, row_medecin[1]))
                req = cursor.fetchone()
                if req == None:
                    break
                if req[6] == 1:
                    if heure_debut.repr == e.Heure(0, 0).repr:
                        heure_debut = e.Heure(heure, minute)
                    duree += 15
                if duree == duree_rdv:
                    liste_heure_dispo.append(heure_debut.repr)
                    heure_debut = e.Heure(0, 0)
                    duree = 0
                if req[6] == 0:
                    heure_debut = e.Heure(0, 0)
                    duree = 0
        dictionnaire_rdv_dispos_par_medecin[motif] = liste_heure_dispo
    return dictionnaire_rdv_dispos_par_medecin


dictionnaire = creneau_dispo_motif('vaccin')
print(dictionnaire)

con.close()