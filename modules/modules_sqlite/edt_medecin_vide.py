import sqlite3
from . import emploidutemps as e
from . import lire_sql as lsql

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

def edt_medecin_vide(medecin, horaire_lundi, horaire_mardi, horaire_mercredi, horaire_jeudi, horaire_vendredi, horaire_samedi):
    '''Crée l'emploi du temps vide pour un médecin pendant un an (mêmes horaires pour toute l'année)'''
    heure_lundi_debut, heure_lundi_fin = horaire_lundi
    heure_mardi_debut, heure_mardi_fin = horaire_mardi
    heure_mercredi_debut, heure_mercredi_fin = horaire_mercredi
    heure_jeudi_debut, heure_jeudi_fin = horaire_jeudi
    heure_vendredi_debut, heure_vendredi_fin = horaire_vendredi
    heure_samedi_debut, heure_samedi_fin = horaire_samedi
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
    Liste_heures = [horaire_lundi_debut, horaire_lundi_fin, horaire_mardi_debut, horaire_mardi_fin, horaire_mercredi_debut, horaire_mercredi_fin, horaire_jeudi_debut, horaire_jeudi_fin, horaire_vendredi_debut, horaire_vendredi_fin, horaire_samedi_debut, horaire_samedi_fin]
    edt = {}
    #construit l'emploi du temps semaine par semaine
    con_1 = lsql.connection_bdd_calendrier()
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nom_jour=?', ['Lundi'])
    rows = cursor_1.fetchall()
    for (i, row) in enumerate(rows): #Un row = un lundi
        id_lundi = row[0]
        liste_id = []
        for i in range(6):
            liste_id.append(id_lundi)
            id_lundi += 1
        cursor_1.executemany('SELECT * FROM calendrier WHERE id_jour=?', liste_id)
        semaine = cursor_1.fetchall()
        con = lsql.connection_bdd()
        cursor = con.cursor()
        liste_jour_i = []
        liste_jour_i_pour_rdv_dispos = []
        heure_debut = Liste_heures[2*i]
        heure_fin = Liste_heures[2*i+1]
        if heure_debut != None and heure_fin != None:
            if heure_debut < e.Heure(12, 0):
                for heure in range(heure_debut.heure, 12):
                    if heure_debut.minute != 0:
                        for minute in range(heure_debut.minute, 46, 15):
                            liste_jour_i.append(e.Heure(heure, minute))
                    else:
                        for minute in range(0, 46, 15):
                            liste_jour_i.append(e.Heure(heure, minute))
            if heure_fin > e.Heure(13, 0):
                for heure in range(13, heure_fin.heure):
                    for minute in range(0, 46, 15):
                        liste_jour_i.append(e.Heure(heure, minute))
            liste_jour_i.append(heure_fin)
            liste_jour_i_pour_rdv_dispos.append((medecin, semaine[i][1], semaine[i][2], semaine[i][3], semaine[i][4]))
            liste_jour_i_pour_rdv_dispos += liste_jour_i
        cursor.executemany('INSERT INTO rdv_dispos VALUES (?, ?, ?, ?, ?, ?, ?)', liste_jour_i_pour_rdv_dispos)
        edt[JOURS[i]] = liste_jour_i
    return edt

edt = edt_medecin_vide("rourajules@bing.fr", "08:00", "19:00", "09:00", "17:00", "08:30", "17:45", "09:45", "18:00", "08:15", "19:00", "", "")
print(edt)