'''Fonction qui n'a pas servi dans le projet'''
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
    '''Remplace dispo = 0 en dispo = 1 sur la base de données rdv_dispos et supprime le rdv dans edt'''
    if not rdp.rdv_dispo(jour, mois, annee, heure, minute, medecin):
        cursor.execute('DELETE FROM rdv_dispos WHERE jour=? AND mois=? AND annee=? AND heure=? AND minute=? AND medecin=?', (jour, mois, annee, heure, minute, medecin))
        cursor.execute('INSERT INTO rdv_dispos VALUES (?, ?, ?, ?, ?, ?, ?)', (jour, mois, annee, heure, minute, medecin, 1))
        cursor.execute('DELETE FROM edt WHERE jour=? AND mois=? AND annee=? AND heure=? AND minute=? AND medecin=?', (jour, mois, annee, heure, minute, medecin))
        con.commit()
        con.close()
    return 'Le rendez-vous a été annulé'


