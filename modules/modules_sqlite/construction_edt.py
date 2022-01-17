import sqlite3

def connection(bdd):
    try:
        connect = sqlite3.connect(bdd)
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')


def nom_jour(jour, mois, annee):
    con_1 = connection('calendrier.db')
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nb_jour=? AND mois_jour=? AND annee=?', (jour, mois, annee))
    req = cursor_1.fetchone()
    con_1.close()
    return req[1]

con = connection('donnees.db')
cursor = con.cursor()

def construction_edt(medecin, jour, mois, annee, heure, minute, motif):
    nom_du_jour = nom_jour(jour, mois, annee)
    cursor.execute('SELECT * FROM rdv_dispos WHERE medecin=? AND jour=? AND mois=? AND annee=? AND heure=? AND minute=?', ([medecin], jour, mois, annee, heure, minute))
    dispo = cursor.fetchone()[6]
    if dispo == 1:
        cursor.execute('SELECT * FROM rdvs WHERE motif=?', [motif])
        duree = cursor.fetchone()[2]
        cursor.execute('INSERT INTO edt VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', ([medecin], nom_du_jour, jour, mois, annee, heure, minute, motif, duree))
    return 'Le rendez-vous a été ajouté'

    
