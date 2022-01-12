import sqlite3
import emploidutemps as e

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
    return req[1]

con = connection('donnees.db')
cursor = con.cursor()


def supprimer_rdv_passe(jour, mois, annee):
    ajd = e.Jour(nom_jour(jour, mois, annee), jour, mois, annee)
    cursor.execute('SELECT * FROM rdv_dispos')
    rows = cursor.fetchall()
    liste_jour = []
    for row in rows:
        jour = e.Jour(nom_jour(row[0], row[1], row[2]), row[0], row[1], row[2])
        if jour < ajd:
            liste_jour.append((row[0], row[1], row[2]))
    cursor.executemany('DELETE FROM rdv_dispos WHERE jour=? AND mois=? AND annee=?', liste_jour)
    con.commit()
    con.close()
    return 'Le rendez-vous a été supprimé'

supprimer_rdv_passe(1, 3, 2022)
