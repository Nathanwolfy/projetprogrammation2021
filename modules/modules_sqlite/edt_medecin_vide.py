import sqlite3
import emploidutemps as e
from . import lire_sql as lsql

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

def edt_medecin_vide(medecin, heure_lundi_debut, heure_lundi_fin, heure_mardi_debut, heure_mardi_fin, heure_mercredi_debut, heure_mercredi_fin, heure_jeudi_debut, heure_jeudi_fin, heure_vendredi_debut, heure_vendredi_fin, heure_samedi_debut, heure_samedi_fin):
    '''Peut créer l'emploi du temps vide pour un médecin pour un an (mêmes horaires pour toute l'année), mais va construire l'emploi du temps vide pour 2 mois'''
    #convertit le string en objet de classe Heure
    if heure_lundi_debut != "" and heure_lundi_fin != "":
            horaire_lundi_debut = e.convert(heure_lundi_debut)
            horaire_lundi_fin = e.convert(heure_lundi_fin)
    else:
        horaire_lundi_debut = None
        horaire_lundi_fin = None
    if heure_mardi_debut != "" and heure_mardi_fin != "":
        horaire_mardi_debut = e.convert(heure_mardi_debut)
        horaire_mardi_fin = e.convert(heure_mardi_fin)
    else:
        horaire_mardi_debut = None
        horaire_mardi_fin = None
    if heure_mercredi_debut != "" and heure_mercredi_fin != "":
        horaire_mercredi_debut = e.convert(heure_mercredi_debut)
        horaire_mercredi_fin = e.convert(heure_mercredi_fin)
    else:
        horaire_mercredi_debut = None
        horaire_mercredi_fin = None
    if heure_jeudi_debut != "" and heure_jeudi_fin != "":
        horaire_jeudi_debut = e.convert(heure_jeudi_debut)
        horaire_jeudi_fin = e.convert(heure_jeudi_fin)
    else:
        horaire_jeudi_debut = None
        horaire_jeudi_fin = None
    if heure_vendredi_debut != "" and heure_vendredi_fin != "":
        horaire_vendredi_debut = e.convert(heure_vendredi_debut)
        horaire_vendredi_fin = e.convert(heure_vendredi_fin)
    else:
        horaire_vendredi_debut = None
        horaire_vendredi_fin = None
    if heure_samedi_debut != "" and heure_samedi_fin != "":
        horaire_samedi_debut = e.convert(heure_samedi_debut)
        horaire_samedi_fin = e.convert(heure_samedi_fin)
    else:
        horaire_samedi_debut = None
        horaire_samedi_fin = None
    liste_heures = [horaire_lundi_debut, horaire_lundi_fin, horaire_mardi_debut, horaire_mardi_fin, horaire_mercredi_debut, horaire_mercredi_fin, horaire_jeudi_debut, horaire_jeudi_fin, horaire_vendredi_debut, horaire_vendredi_fin, horaire_samedi_debut, horaire_samedi_fin]
    #construit l'emploi du temps semaine par semaine
    con_1 = lsql.connection_bdd_calendrier()
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nom_jour=?', ['Lundi'])
    rows = cursor_1.fetchall()
    premier_mois = rows[0][3]
    annee = rows[0][4]
    for row in rows: #Un row = un lundi
        if ((row[3] == premier_mois and row[4] == annee) or (row[3] == premier_mois + 1 and row[4] == annee)) or (premier_mois == 12 and (row[3] == 12 or row[3] == 1)): #Arbitrairement on s'arrête au bout de 2 mois
            id_lundi = row[0]
            liste_id = []
            for j in range(6): #pour la semaine (sauf le dimanche)
                liste_id.append(id_lundi)
                cursor_1.execute('SELECT * FROM calendrier WHERE id_jour=?', (id_lundi,)) #prend chaque jour de la semaine
                jour_de_la_semaine = cursor_1.fetchone()
                id_lundi += 1
                con = lsql.connection_bdd()
                cursor = con.cursor()
                liste_jour_j_pour_rdv_dispos = [] #va être remplie des horaires de la journée
                heure_debut = liste_heures[2*j]
                heure_fin = liste_heures[2*j+1]
                if heure_debut != None and heure_fin != None:
                    if heure_debut < e.Heure(12, 0): #Si le médecin travaille le matin
                        for heure in range(heure_debut.heure, 12):
                            if heure_debut.minute != 0: #S'il commence à une heure pas ronde
                                for minute in range(heure_debut.minute, 46, 15):
                                    liste_jour_j_pour_rdv_dispos.append((jour_de_la_semaine[2], jour_de_la_semaine[3], jour_de_la_semaine[4], heure, minute, medecin, 1))
                            else:
                                for minute in range(0, 46, 15):
                                    liste_jour_j_pour_rdv_dispos.append((jour_de_la_semaine[2], jour_de_la_semaine[3], jour_de_la_semaine[4], heure, minute, medecin, 1))
                    if heure_fin > e.Heure(13, 0): #Si le médecin travaille l'après-midi
                        for heure in range(13, heure_fin.heure):
                            for minute in range(0, 46, 15):
                                liste_jour_j_pour_rdv_dispos.append((jour_de_la_semaine[2], jour_de_la_semaine[3], jour_de_la_semaine[4], heure, minute, medecin, 1))
                    liste_jour_j_pour_rdv_dispos.append((jour_de_la_semaine[2], jour_de_la_semaine[3], jour_de_la_semaine[4], heure_fin.heure, heure_fin.minute, medecin, 1)) #dernier horaire de la journée
                cursor.executemany('INSERT INTO rdv_dispos VALUES (?, ?, ?, ?, ?, ?, ?)', liste_jour_j_pour_rdv_dispos)
                con.commit()
    con_1.close()
    con.close()
    return('L\'emploi du temps a été ajouté') 

