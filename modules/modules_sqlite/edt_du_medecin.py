import sqlite3
import emploidutemps as e
import time

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

def nb_jours_dans_un_mois(mois, annee): 
    if mois == 2: #Février
        if annee % 4 == 0:
            return 29 #année bissextile
        else:
            return 28 #année non bissextile
    elif mois < 8 and mois%2 == 1:
        return 31
    elif mois >=8 and mois%2 == 0:
        return 31
    return 30

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

def lundi_de_la_semaine(nom_jour, jour, mois, annee):
    '''Cette fonction renvoie le lundi (jour, mois, annee) de la semaine'''
    indice = JOURS.index(nom_jour)
    for i in range(indice):
        if jour == 1:
            if mois == 1:
                jour = 31
                mois = 12
                annee = annee - 1
            else:
                mois -= 1
                jour = nb_jours_dans_un_mois(mois, annee)
        else:
            jour -= 1
    return (jour, mois, annee)

def return_edt(medecin):
    '''Cette fonction retourne l'emploi du temps de la semaine actuelle d'un medecin particulier '''
    edt = {}
    #Renvoie l'emploi du temps de la semaine actuelle donc on a besoin de la date d'aujourd'hui
    now = time.localtime(time.time())
    actual_time = time.strftime("%a %d %m %Y", now) #nom_jour (english) nb_jour mois annee
    nom_jour = JOURS[DAYS.index(actual_time[:3])]
    date_actuelle = nom_jour + ' ' + actual_time[4:]
    D = date_actuelle.split()
    jour = int(D[1])
    mois = int(D[2])
    annee = int(D[3])
    lundi = lundi_de_la_semaine(nom_jour, jour, mois, annee)
    jour_i = lundi[0]
    mois_i = lundi[1]
    annee_i = lundi[2]
    for i in range(6):
        cursor.execute('SELECT * FROM edt WHERE medecin=? AND jour=? AND mois=? AND annee=?', (medecin, jour_i, mois_i, annee_i))
        rows = cursor.fetchall()
        liste_horaire = [] #prend les heures du début du rendez-vous
        for row in rows:
            heure = row[5]
            minute = row[6]
            horaire = e.Heure(heure, minute)
            liste_horaire.append(horaire)
            liste_horaire.sort()
        liste_creneau = [] #prend les créneaux : ex : [08:00-08:45, 15:15-16:30]
        for h in liste_horaire:
            cursor.execute('SELECT * FROM edt WHERE medecin=? AND jour=? AND mois=? AND annee=? AND heure=? AND minute=?', (medecin, jour_i, mois_i, annee_i, h.heure, h.minute))
            duree = int(cursor.fetchone()[8])
            duree_boucle = duree // 15
            heure_i = h.heure
            minute_i = h.minute
            horaire_i = e.Heure(heure_i, minute_i)
            for j in range(duree_boucle):
                if horaire_i.minute == 45:
                    horaire_i.heure += 1
                    horaire_i.minute = 0
                    horaire_i = e.Heure(horaire_i.heure, horaire_i.minute)
                else:
                    horaire_i.minute += 15
                    horaire_i = e.Heure(horaire_i.heure, horaire_i.minute)
            liste_creneau.append(h.repr + '-' + horaire_i.repr)
        edt[JOURS[i]] = liste_creneau
        if jour_i < nb_jours_dans_un_mois(mois_i, annee_i):
            jour_i += 1
        else:
            if mois_i == 12:
                mois_i = 1
                annee_i += 1
            else:
                mois_i += 1
            jour_i = 1
    return edt
                      

con.close()

