'''Fonction qui n'a pas servi dans le projet'''
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
    con_1.close()
    return req[1]

con = connection('donnees.db')
cursor = con.cursor()


def supprimer_rdv_passe(jour, mois, annee):
    '''Cette fonction supprime tous les rendez-vous antérieurs à un jour donné'''
    ajd = e.Jour(nom_jour(jour, mois, annee), jour, mois, annee)
    cursor.execute('SELECT * FROM rdv_dispos')
    rows = cursor.fetchall()
    liste_jour = [] #prend tous les jours antérieurs au jour donné
    for row in rows: #chaque row correspond à un rendez-vous
        jour = e.Jour(nom_jour(row[0], row[1], row[2]), row[0], row[1], row[2])
        if jour < ajd:
            liste_jour.append((row[0], row[1], row[2]))
    cursor.executemany('DELETE FROM rdv_dispos WHERE jour=? AND mois=? AND annee=?', liste_jour)
    con.commit()
    con.close()
    return 'Les rendez-vous ont été supprimés'


