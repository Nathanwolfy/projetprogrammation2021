import sqlite3
import emploidutemps as e

def connection(bdd):
    try:
        connect = sqlite3.connect(bdd)
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')

con_1 = connection('calendrier.db')
cursor_1 = con_1.cursor()
def nom_jour(jour, mois, annee):
    cursor_1.execute('SELECT * FROM calendrier ')

con = connection('donnees.db')
cursor = con.cursor()


def supprimer_rdv_passe(jour, mois, annee):
    ajd = e.Jour()
    cursor.execute('SELECT * FROM rdv_dispos')
    rows = cursor.fetchall()
    liste_jour = []
    for row in rows:
        
