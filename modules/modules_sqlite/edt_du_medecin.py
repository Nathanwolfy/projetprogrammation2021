import sqlite3
from . import emploidutemps as e
from . import lire_sql as lsql
import time

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

def nb_jours_dans_un_mois(mois, annee): 
    '''Cette fonction renvoie le nombre de jours qu'il y a dans un certain mois'''
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

def nom_jour(jour, mois, annee):
    '''Cette fonction renvoie le nom du jour grâce à la base de données calendrier'''
    con_1 = lsql.connection_bdd_calendrier()
    cursor_1 = con_1.cursor()
    cursor_1.execute('SELECT * FROM calendrier WHERE nb_jour=? AND mois_jour=? AND annee=?', (jour, mois, annee))
    req = cursor_1.fetchone()
    con_1.close()
    return req[1]

def lundi_de_la_semaine(nom_jour, jour, mois, annee):
    '''Cette fonction renvoie le lundi (jour, mois, annee) de la semaine'''
    indice = JOURS.index(nom_jour)
    for i in range(indice):
        if jour == 1: #Si c'est le premier jour du mois, le jour d'avant dépend du mois 
            if mois == 1: #Janvier
                jour = 31
                mois = 12
                annee = annee - 1
            else:
                mois -= 1
                jour = nb_jours_dans_un_mois(mois, annee) #le jour d'avant correspond au nombre de jours qu'il y a dans le mois précédent
        else:
            jour -= 1
    return (jour, mois, annee)

def return_edt(medecin):
    '''Cette fonction retourne l'emploi du temps de la semaine actuelle d'un medecin particulier '''
    con = lsql.connection_bdd()
    cursor = con.cursor()
    edt = {}
    #Chaque jour prend en info les horaires de rdv et à chaque horaire est associé le nom et prénom du patient, le motif, et une remarque s'il y en a une
    lundi_ = {} #lundi est une variable définie après
    mardi = {}
    mercredi = {}
    jeudi = {}
    vendredi = {}
    samedi = {}
    journee = [lundi_, mardi, mercredi, jeudi, vendredi, samedi]
    #Renvoie l'emploi du temps de la semaine actuelle donc on a besoin de la date d'aujourd'hui
    now = time.localtime(time.time())
    actual_time = time.strftime("%a %d %m %Y", now) #nom_jour (english) jour mois annee
    nom_jour = JOURS[DAYS.index(actual_time[:3])]
    date_actuelle = nom_jour + ' ' + actual_time[4:]
    D = date_actuelle.split()
    jour = int(D[1])
    mois = int(D[2])
    annee = int(D[3])
    lundi = lundi_de_la_semaine(nom_jour, jour, mois, annee) #La semaine commence le lundi
    jour_i = lundi[0]
    mois_i = lundi[1]
    annee_i = lundi[2]
    for i in range(6): #Pour une semaine (sans le dimanche)
        le_jour_de_la_semaine = journee[i]
        cursor.execute('SELECT * FROM edt WHERE medecin=? AND jour=? AND mois=? AND annee=?', (medecin, jour_i, mois_i, annee_i)) #sélectionne les rendez-vous du jour de la semaine en fonction du médecin
        rows = cursor.fetchall() #Tous les rendez-vous d'un certain jour de la semaine
        liste_horaire = [] #prend les heures du début du rendez-vous
        for row in rows:
            heure = row[5]
            minute = row[6]
            horaire = e.Heure(heure, minute)
            liste_horaire.append(horaire)
            #les valeurs d'une base de données ne sont pas triées
            liste_horaire.sort() 
        liste_creneau = [] #prend les créneaux : ex : [08:00-08:45, 15:15-16:30]
        for h in liste_horaire: #chaque h correspond à l'heure de début du rdv
            cursor.execute('SELECT * FROM edt WHERE medecin=? AND jour=? AND mois=? AND annee=? AND heure=? AND minute=?', (medecin, jour_i, mois_i, annee_i, h.heure, h.minute))
            c = cursor.fetchone()
            mail_patient = c[10]
            cursor.execute('SELECT * FROM patients WHERE mail=?', [mail_patient])
            c1 = cursor.fetchone() #on veut renvoyer le nom complet du patient
            prenom_patient = c1[0]
            nom_patient = c1[1]
            motif = c[7]
            if c[9] != None:
                note = c[9]
                le_jour_de_la_semaine[h] = ['motif : ' + motif, 'remarque : ' + note, 'patient : ' + prenom_patient + ' ' + nom_patient]
            else:
                le_jour_de_la_semaine[h] = ['motif : ' + motif, 'patient : ' + prenom_patient + ' ' + nom_patient]
            duree = c[8] #le créneau dépend de la durée du rdv, donc il faut déterminer l'heure de fin du rdv
            #détermination de l'heure de fin du rdv
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
        #jour suivant
        if jour_i < nb_jours_dans_un_mois(mois_i, annee_i): 
            jour_i += 1
        else:
            if mois_i == 12:
                mois_i = 1
                annee_i += 1
            else:
                mois_i += 1
            jour_i = 1
    con.close()
    return edt
