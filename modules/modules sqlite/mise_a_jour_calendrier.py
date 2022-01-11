import sqlite3
import time

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Wen", "Sat", "Sun"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

def nb_jours_dans_un_mois(mois, annee): 
    if mois == 2: #Février
        if annee % 4 == 0:
            return 29 #année bissextile
        else:
            return 28 #année non bissextile
    elif mois%2 == 0:
        return 31
    elif mois == 7:
        return 31
    return 30

now = time.localtime(time.time())
actual_time = time.strftime("%a %d %m %Y", now) #nom_jour (english) nb_jour mois annee
print(actual_time)
nom_jour = JOURS[DAYS.index(actual_time[:3])]
date_actuelle = nom_jour + ' ' + actual_time[4:]
print(date_actuelle)
nb_jour = int(date_actuelle[6:8])
mois_jour = int(date_actuelle[10:12])
annee = int(date_actuelle[14:])
annee_dans_un_an = annee + 1
date_dans_un_an = date_actuelle[:14] + str(annee_dans_un_an) 
print(date_dans_un_an)

def connection():
    try:
        connect = sqlite3.connect('calendrier.db')
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')


con = connection()
cursor = con.cursor()

cursor.execute('SELECT id_jour FROM calendrier')
rows = cursor.fetchall()
cursor.execute('SELECT nom_jour FROM calendrier WHERE id_jour=?', (len(rows),))
nom_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT nb_jour FROM calendrier WHERE id_jour=?', (len(rows),))
nb_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT mois_jour FROM calendrier WHERE id_jour=?', (len(rows),))
mois_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT annee FROM calendrier WHERE id_jour=?', (len(rows),))
annee_dernier_jour = cursor.fetchone()[0]
if nb_dernier_jour < 10:
    str_nb_dernier_jour = '0' + str(nb_dernier_jour)
else:
    str_nb_dernier_jour = str(nb_dernier_jour)
if mois_dernier_jour < 10:
    str_mois_dernier_jour = '0' + str(mois_dernier_jour)
else:
    str_mois_dernier_jour = str(mois_dernier_jour)
dernier_jour = nom_dernier_jour + ' ' + str_nb_dernier_jour + ' ' + str_mois_dernier_jour + ' ' + str(annee_dernier_jour)
print(dernier_jour)

id = len(rows)
#complète le calendrier pour qu'on puisse potentiellement prendre un rdv un an à l'avance 

list_jour = []
while dernier_jour != date_dans_un_an:
    if JOURS.index(nom_jour) == len(JOURS) - 1:
        nom_jour = "Lundi"
    else:
        indice = JOURS.index(nom_jour)
        nom_jour = JOURS[indice + 1]
    if nb_jour < nb_jours_dans_un_mois(mois_jour, annee):
        nb_jour += 1
        list_jour.append((id, nom_jour, nb_jour, mois_jour, annee))
        id += 1
        if nb_jour < 10:
            str_nb_jour = '0' + str(nb_jour)
        else:
            str_nb_jour = str(nb_jour)
        if mois_jour < 10:
            str_mois_jour = '0' + str(mois_jour)
        else:
            str_mois_jour = str(mois_jour)
        dernier_jour = nom_jour + ' ' + str_nb_jour + ' ' + str_mois_jour + ' ' + str(annee)
    else:
        if mois_jour == 12:
            mois_jour = 1
            annee += 1
        else:
            mois_jour += 1
        nb_jour = 1
        list_jour.append((id, nom_jour, nb_jour, mois_jour, annee))
        id += 1
        if nb_jour < 10:
            str_nb_jour = '0' + str(nb_jour)
        else:
            str_nb_jour = str(nb_jour)
        if mois_jour < 10:
            str_mois_jour = '0' + str(mois_jour)
        else:
            str_mois_jour = str(mois_jour)
        dernier_jour = nom_jour + ' ' + str_nb_jour + ' ' + str_mois_jour + ' ' + str(annee)

cursor.executemany("INSERT INTO calendrier VALUES (?, ?, ?, ?, ?)", list_jour)
con.commit()
con.close()