import sqlite3
import rdv_dispo_pris as rdp

def connection():
    try:
        connect = sqlite3.connect('donnees.db')
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')

con = connection()
cursor = con.cursor

def annuler_rdv(jour, mois, annee, heure, minute, medecin):
    if not rdp.rdv_dispo(jour, mois, annee, heure, minute, medecin):
        cursor.execute('DELETE FROM rdv_dispos WHERE jour=? AND mois=? AND annee=? AND heure=? AND minute=? AND medecin=?', (jour, mois, annee, heure, minute, medecin))
        cursor.execute('INSERT INTO rdv_dispos VALUES (?, ?, ?, ?, ?, ?, ?)', (jour, mois, annee, heure, minute, medecin, 1))
    return 'Le rendez-vous a été annulé'


